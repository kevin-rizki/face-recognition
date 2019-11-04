import cv2
import numpy as np
import pickle
from extract import *
from vector import *

dbfile = open("pins.db", "rb")
db = pickle.load(dbfile)
print(db)
sim = 0
name = "Not found"
dsc = extractFeatures("PINS/pins_Aaron Paul/Aaron Paul130_215.jpg")
for e in db:
    k = db[e]
    x = calcCosineSimilarity(dsc, k["desc"])
    print(x, e)
    if x > sim:
        sim  = x
        name = e

print("Match with:", name, "(", sim, ")")
