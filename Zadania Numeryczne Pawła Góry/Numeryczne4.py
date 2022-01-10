#!/usr/bin/env python

import sys
import numpy as np
import math


def HouseHolder(Vector):
    Identity = np.identity(Vector.size)
    e = np.zeros(Vector.size)
    e[0] = 1.0
    e *= np.linalg.norm(Vector, 2)
    Vector = Vector - e
    MatVector = np.zeros((Vector.size,Vector.size))
    MatVector[0] += Vector
    MatVector = np.dot(np.transpose(MatVector), MatVector)
    HouseHolder = Identity - 2.0 / pow(np.linalg.norm(Vector), 2) * MatVector
    return HouseHolder

def ToTriDiagonal(HouseHolder):
    ToTri = np.identity(6)
    a = 6 - HouseHolder.shape[0]
    for i in range (a, 6, 1):
        for j in range (a, 6, 1):
            ToTri[i,j] = HouseHolder[i-a,j-a]
    return ToTri

def MatrixBetweenMatrixes(A, BetweenMat):
    AHT = np.dot(A, np.transpose(BetweenMat))
    HAHT = np.dot(BetweenMat, AHT)
    return HAHT

def Givens (i, Matrix):
    Identity = np.identity(Matrix[0].size)
    Vector = np.array(Matrix[i])
    c = Vector[i] / math.sqrt(pow(Vector[i], 2) + pow(Vector[i+1], 2))
    s = Vector[i+1] / math.sqrt(pow(Vector[i], 2) + pow(Vector[i+1], 2))
    Identity[i,i] = c
    Identity[i+1, i+1] = c
    Identity[i+1, i] = -s
    Identity[i, i+1] = s
    return Identity

def RQ(matrix):
    for i in range (matrix[0].size - 1):
        print (Givens(i, matrix))
        matrix = MatrixBetweenMatrixes(matrix, Givens(i, matrix))
    return matrix

if (__name__ == "__main__"):
    matrix = np.array([[19.0/12.0,13.0/12.0,5.0/6.0,5.0/6.0,13.0/12.0,-17.0/12.0], 
                    [13.0/12.0, 13.0/12.0, 5.0/6.0, 5.0/6.0, -11.0/12.0, 13.0/12.0],
                    [5.0/6.0, 5.0/6.0, 5.0/6.0, -1.0/6.0, 5.0/6.0, 5.0/6.0],
                    [5.0/6.0, 5.0/6.0, -1.0/6.0, 5.0/6.0, 5.0/6.0, 5.0/6.0],
                    [13.0/12.0, -11.0/12, 5.0/6.0, 5.0/6.0, 13.0/12.0, 13.0/12.0],
                    [-17.0/12.0, 13.0/12.0, 5.0/6.0, 5.0/6.0, 13.0/12.0, 19.0/12.0]])
    for i in range (matrix[0].size - 2):
        H = HouseHolder(np.array(matrix[i][(i+1):6]))
        TT = ToTriDiagonal(H)
        matrix = MatrixBetweenMatrixes(matrix, TT)

    a = 1
    while (a > 0.00000001):
        matrixOld = matrix
        matrix = RQ(matrix)
        a = abs(np.linalg.norm(matrixOld - matrix, 2))
    
    for j in range(matrix[0].size):
        sys.stdout.write("[")
        for i in range (matrix[0].size):
            sys.stdout.write(f'{matrix[j][i]:.8f}')
            if(i != matrix[0].size - 1):
                sys.stdout.write(" ")
        sys.stdout.write("]\n")
    sys.stdout.write("\n")
