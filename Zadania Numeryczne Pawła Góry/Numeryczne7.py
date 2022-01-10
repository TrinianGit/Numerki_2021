#!/usr/bin/env python

import math
import numpy as np
import sys
from matplotlib import pyplot as plt

def PolyCoefficients(x, coeffs):
    o = len(coeffs)
    y = 0
    for i in range(o):
        y += coeffs[(o-1)-i]*x**i
    return y



def GetRidOfLower(matrix, bVector):
    size = math.sqrt(matrix.size)
    for i in range(int(size)):
        devider = matrix[i,i]
        for j in range(int(size)):
            matrix[i,j] /= devider
        bVector[i] /= devider
        for j in range(int(size)):
            if (i < j):
                multi = matrix[j,i]
                matrix[j] = matrix[j] - matrix[i] * multi
                bVector[j] = bVector[j] - bVector[i] * multi


def GetRidOfUpper(matrix, bVector):
    size = math.sqrt(matrix.size)
    for i in range(int(size)-1,-1,-1):
        for j in range(int(size)-1,-1,-1):
            if (i > j):
                multi = matrix[j,i]
                matrix[j] = matrix[j] - matrix[i] * multi
                bVector[j] = bVector[j] - bVector[i] * multi

def PrintVector(vector):
    for i in range(vector.shape[0]):
        sys.stdout.write("[")
        sys.stdout.write("{:.4f}".format(vector[i]))
        sys.stdout.write("]\n")

if(__name__ == "__main__"):

    fVector = np.array([0.687959, 0.073443,-0.517558,-1.077264,-1.600455,-2.080815,-2.507266,-2.860307])
    yVector = np.array (fVector)
    xVector = np.array([0.062500, 0.187500, 0.312500, 0.437500, 0.562500, 0.687500, 0.812500, 0.937500])
    matrix = np.identity(8)
    for i in range (8):
        for j in range (7, -1, -1):
            matrix[i, j] = pow(xVector[i], 7-j)
    GetRidOfLower(matrix, fVector)
    GetRidOfUpper(matrix, fVector)
    x = np.linspace(-1, 1)
    plt.plot(x, PolyCoefficients(x, fVector))
    for i in range (8):
        x0 = xVector[i]
        y0 = yVector[i]
        plt.plot(x0, y0, '-o')
    plt.show()
    PrintVector (fVector)