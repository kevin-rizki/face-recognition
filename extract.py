# Import necessary modules
import cv2
import numpy as np
import scipy
from scipy.misc import imread
import cPickle as pickle
import random
import os
import matplotlib.pyplot as plt

def extractFeatures(imgPath, vectorSize = 32):
    # Get image data from P A T H
    image = imread(imgPath, mode = "RGB")
    descriptors = None
    # Extract 
    try:
        alg = cv2.KAZE_create()
        keypoints = alg.detect(image)
        keypoints = sorted(keypoints, key = lambda x: -x.response)[0:vectorSize]
        keypoints, descriptors = alg.compute(image, keypoints)
        descriptors = descriptors.flatten()
        dscsize = vectorSize * 64
        if descriptors.size < dscsize:
            descriptors = np.concatenate([descriptors, np.zeros(dscsize - descriptors.size)])
        elif descriptors.size > dscsize:
            descriptors = descriptors[0:dscsize]
    except cv2.error as e::
        print 'Error while extracting image: ', e
        return None
    return descriptors

def generatePickleFromBatch(pckPath, imgsPath):
    files = [os.path.join(imgsPath, p) for p in sorted(os.listdir(imgsPath))]

    result = {}
    for f in files:
        print('Extracting features from image %s' %(f))
        name = f.split('/')[-1].lower()
        result[name] = extractFeatures(f)

    # saving all our feature vectors in pickled file
    with open(pckPath, 'w') as fp:
        pickle.dump(result, fp)

