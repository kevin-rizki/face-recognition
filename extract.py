import cv2
import numpy as np
import scipy
import random
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Wrote using jupyter, changed the working directory
# os.chdir('F:/Docs/Kuliah/AlGeo/Tubes Algeo')

# Getting images
def TraverseImages(root_path='./PINS'):
    for dir_name, sub_dir_list, file_list in os.walk(root_path):
        print(file_list)

# Image path generator
def ImagePath(imgdir):
    temp = './PINS/pins_Aaron Paul/%s' %(imgdir)
    return temp

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
        bf = cv2.BFMatcher(cv2.NORM_L1)
        matches = bf.knnMatch(desc1, desc2, k = 2)
        
        good = []
        for m, n in matches:
            if m.distance < 0.9 * n.distance :
                good.append([m])
                
        return len(good)
    except cv2.error as e:
        print('Error: %s' %(e))