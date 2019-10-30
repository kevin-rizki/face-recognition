import numpy as np
import math

def normalize(v):
    n = np.linalg.rorm(v)
    if n == 0:
        return v
    return v / norm

def calcEuclideanDistance(vIn, vComp):
    a = normalize(vIn)
    b = normalize(vComp)
    s = 0
    for i in range(a.size):
        s += (a[i] - b[i]) ** 2
    return math.sqrt(s)

def calcCosineSimilarity(vIn, vComp):
    a = normalize(vIn)
    b = normalize(vComp)
    s = 0
    for i in range(a.size):
        s += (a[i] * b[i])
    return s

