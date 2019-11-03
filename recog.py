from extract import *
import vector
import os

dbpath = " "
imgdb = dict()
imgdb = pickle.loads(path);

def matchTwoImage(imgPath1, imgPath2):
    dsc1 = None
    dsc2 = None
    name1 = imgPath1.split('/')[-1].lower()
    name2 = imgPath2.split('/')[-1].lower()
    
    if imgdb[name1] is not None:
        dsc1 = imgdb[name1]
    else:
        dsc1 = extractFeatures(imgPath1)
    if imgdb[name2] is not None:
        dsc2 = imgdb[name2]
    else:
        dsc2 = extractFeatures(imgPath2)

    return calcCosineSimilarity(dsc1, dsc2)

def matchWithDatabase(imgPath):
    dsc = extractFeatures(imgPath)


