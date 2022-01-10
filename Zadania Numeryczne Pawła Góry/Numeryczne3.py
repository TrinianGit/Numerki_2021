#!/usr/bin/env python

import sys
import numpy as np


def PowerIterationFirst(matrix, vector):
    Vector_norm = vector/np.linalg.norm(vector,2)
    lamb = np.dot(np.dot(matrix, Vector_norm), Vector_norm) / np.dot(Vector_norm, Vector_norm)
    while (abs(np.linalg.norm(np.dot(matrix, Vector_norm) - lamb * Vector_norm, 2)) > 0.00000001):
        Vector_norm = np.dot(matrix, Vector_norm)
        Vector_norm = Vector_norm/np.linalg.norm(Vector_norm, 2)
        lamb = np.dot(np.dot(matrix, Vector_norm), Vector_norm) / np.dot(Vector_norm, Vector_norm)
    return (Vector_norm, lamb)

def PowerIterationSecond(matrix, vector1, vector2):
    Zk = np.dot(matrix, vector1)
    Zk = Zk - vector2 * (np.dot(vector2, Zk))
    ResVector = Zk / np.linalg.norm(Zk)
    lamb = np.dot(Zk, ResVector) / np.dot(ResVector, ResVector)
    
    while (abs(np.linalg.norm(np.dot(matrix,ResVector) - lamb * ResVector, 2)) > 0.000000001):
        Zk = np.dot(matrix, ResVector)
        Zk = Zk - vector2*(np.dot(vector2, Zk))
        ResVector = Zk / np.linalg.norm(Zk)
        lamb = np.dot(Zk, ResVector) / np.dot(ResVector, ResVector)

    return (ResVector, lamb)

def VectorPerpendicular(vector):
    ResultVector = np.array(vector)
    if (vector.size % 2 == 0):
        for i in range (0, vector.size, 2):
            ResultVector[i] *= -1
    else:
        ResultVector[0] = 0.0
        for i in range (1, vector.size + 1, 2):
            ResultVector[i] *= -1
    return ResultVector


if (__name__ == "__main__"):
    print ("Dla macierzy A o strukturze: ")
    Vector = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    matrix = np.array([[19.0/12.0,13.0/12.0,5.0/6.0,5.0/6.0,13.0/12.0,-17.0/12.0], 
                    [13.0/12.0, 13.0/12.0, 5.0/6.0, 5.0/6.0, -11.0/12.0, 13.0/12.0],
                    [5.0/6.0, 5.0/6.0, 5.0/6.0, -1.0/6.0, 5.0/6.0, 5.0/6.0],
                    [5.0/6.0, 5.0/6.0, -1.0/6.0, 5.0/6.0, 5.0/6.0, 5.0/6.0],
                    [13.0/12.0, -11.0/12, 5.0/6.0, 5.0/6.0, 13.0/12.0, 13.0/12.0],
                    [-17.0/12.0, 13.0/12.0, 5.0/6.0, 5.0/6.0, 13.0/12.0, 19.0/12.0]])

    print (matrix)
    vector, lamb = PowerIterationFirst(matrix, Vector)
    print ("Najwieksza waroscia wlasna jest: ")
    print (lamb)
    print ("Odpowiadajacym tej wartosci wlasnej wektorem wlasnym jest np.:")
    print (vector)
    vector2, lamb2 = PowerIterationSecond(matrix, VectorPerpendicular(vector), vector)
    print ("Druga najwieksza waroscia wlasna jest: ")
    print (f'{lamb2:.8f}')
    print ("Odpowiadajacym tej wartosci wlasnej wektorem wlasnym jest np.:")
    sys.stdout.write("[")
    for i in range (vector2.size):
        sys.stdout.write(f'{vector2[i]:.8f}')
        if(i != vector.size - 1):
            sys.stdout.write(" ")
    sys.stdout.write("]\n")