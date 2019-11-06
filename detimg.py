import cv2
import numpy as np
import pickle
from extract import *
from vector import *

dbfile = open("pins.db", "rb")
db = pickle.load(dbfile)
#print(db)
sim = 0
name = "Not found"
dsc = extractFeatures("TestData/pins_Alvaro Morte/Alvaro Morte172_868.jpg")
for e in db:
    k = db[e]
    x = calcEuclideanDistance(dsc, k)
    print(x, e, end = '          ')
    if x > sim:
        sim  = x
        name = e
    print('\r', end= '  ')

print("Match with:", name, "(", sim, ")")
