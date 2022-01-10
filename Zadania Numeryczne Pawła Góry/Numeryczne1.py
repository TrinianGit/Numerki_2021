#!/usr/bin/env python

import math
import numpy as np
import sys

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

def PrintMatrix(matrix):
    size = math.sqrt(matrix.size)
    for i in range(int(size)):
        sys.stdout.write("[")
        for j in range(int(size)):
            sys.stdout.write("{:.8f}".format(matrix[i,j]))
            if (j != int(size) -1):
                sys.stdout.write(", ")
        sys.stdout.write("]\n")

def PrintVector(vector):
    for i in range(vector.shape[0]):
        sys.stdout.write("[")
        sys.stdout.write("{:.8f}".format(vector[i][0]))
        sys.stdout.write("]\n")

if(__name__ == "__main__"):

    b1Vector = np.array([[1.0],[2.0],[3.0],[4.0],[5.0],[6.0],[7.0]])
    matrixA = np.array([[4.0,1.0,0.0,0.0,0.0,0.0,0.0],
                    [1.0,4.0,1.0,0.0,0.0,0.0,0.0],
                    [0.0,1.0,4.0,1.0,0.0,0.0,0.0],
                    [0.0,0.0,1.0,4.0,1.0,0.0,0.0],
                    [0.0,0.0,0.0,1.0,4.0,1.0,0.0],
                    [0.0,0.0,0.0,0.0,1.0,4.0,1.0],
                    [0.0,0.0,0.0,0.0,0.0,1.0,4.0]])
    sys.stdout.write("Dla macierzy A:\n")
    print(matrixA)
    sys.stdout.write("Ktorej rozwiazaniem jest wektor b:\n")
    print(b1Vector)
    sys.stdout.write("Poszukiwanym wektorem jest x:\n")
    GetRidOfLower(matrixA, b1Vector)
    GetRidOfUpper(matrixA, b1Vector)
    PrintVector (b1Vector)

    b2Vector = np.array([[1.0],[2.0],[3.0],[4.0],[5.0],[6.0],[7.0]])

    matrixB = np.array([[4.0,1.0,0.0,0.0,0.0,0.0,1.0],
                    [1.0,4.0,1.0,0.0,0.0,0.0,0.0],
                    [0.0,1.0,4.0,1.0,0.0,0.0,0.0],
                    [0.0,0.0,1.0,4.0,1.0,0.0,0.0],
                    [0.0,0.0,0.0,1.0,4.0,1.0,0.0],
                    [0.0,0.0,0.0,0.0,1.0,4.0,1.0],
                    [1.0,0.0,0.0,0.0,0.0,1.0,4.0]])
    sys.stdout.write("Dla macierzy A:\n")
    print(matrixB)
    sys.stdout.write("Ktorej rozwiazaniem jest wektor b:\n")
    print(b2Vector)
    sys.stdout.write("Poszukiwanym wektorem jest x:\n")
    GetRidOfLower(matrixB, b2Vector)
    GetRidOfUpper(matrixB, b2Vector)
    PrintVector (b2Vector)
