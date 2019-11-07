# Import necessary modules
import cv2
import numpy as np
import scipy
import pickle
import random
import os
import matplotlib.pyplot as plt

def extractFeatures(imgPath, vectorSize = 32):
    # Get image data from P A T H
    image = cv2.imread(imgPath)
    descriptors = None
    # Extract 
    try:
        alg = cv2.KAZE_create()
        keypoints = alg.detect(image)
        keypoints = sorted(keypoints, key = lambda x: -x.response)[0:vectorSize]
        keypoints, descriptors = alg.compute(image, keypoints)
        #keypoints, descriptors = alg.detectAndCompute(image, None)
        descriptors = descriptors.flatten()
        dscsize = vectorSize * 64

        if descriptors.size < dscsize:
            descriptors = np.concatenate([descriptors, np.zeros(dscsize - descriptors.size)])
        elif descriptors.size > dscsize:
            descriptors = descriptors[0:dscsize]
    except cv2.error as e:
        print ('Error while extracting image: ', e)
        return None
    return descriptors

