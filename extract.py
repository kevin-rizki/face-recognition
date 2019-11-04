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
        #keypoints, descriptors = alg.detectAndCompute(imgPath, None)
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

def generatePickleFromBatch(pckPath, imgsPath):
    files = [os.path.join(imgsPath, p) for p in sorted(os.listdir(imgsPath))]

    result = {}
    for f in files:
        print('Extracting features from image %s' %(f))
        name = f.split('/')[-1].lower()
        result[name] = dict()
        result[name]["path"] = f
        result[name]["desc"] = extractFeatures(f)

    # saving all our feature vectors in pickled file
    with open(pckPath, 'ab') as fp:
        pickle.dump(result, fp)
# Image path generator
        
def VectorSize(vec):
    sum = float(0)
    for i in range(len(vec)):
        sum = sum + vec[i] * vec[i]
    return sum**(1/2.0)


# Image Matcher
def ImageMatcher(img_path1, img_path2):
    try:
        # Load image
        img1 = cv2.imread(img_path1)
        img2 = cv2.imread(img_path2)

        # We don't need RGB since we're only detecting a single face per image. Result is a hued grayscale image
        img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        
        # KAZE descriptor
        kaze = cv2.KAZE_create()
        keypt1, desc1 = kaze.detectAndCompute(img1_gray, None)
        keypt2, desc2 = kaze.detectAndCompute(img2_gray, None)

        # desc1 = np.uint8(desc1)
        # desc2 = np.uint8(desc2)
        
        # bf = cv2.BFMatcher(cv2.NORM_HAMMLING)
        # bf = cv2.BFMatcher(cv2.NORM_L1)
        # matches = bf.knnMatch(desc1, desc2, k = 2)
        
        # good = []
        # for m, n in matches:
        #    if m.distance < 0.9 * n.distance :
        #        good.append([m])
        
                
        return desc1
    except cv2.error as e:
        print('Error: %s' %(e))
        
# print(ImageMatcher('./Justin_Bieber_2010_3.jpg', './Justin_Bieber_2010_3.jpg')[0])
