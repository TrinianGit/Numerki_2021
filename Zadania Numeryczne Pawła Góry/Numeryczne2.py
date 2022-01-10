#!/usr/bin/env python

import numpy as np


matrix = {}
Vectorx = np.zeros(128)
bVector = np.ones(128)
Vectorx2 = np.zeros(128)


def GaussSeidel():
    for i in range (128):
        Vectorx[i] = (1.0/matrix.get((i, i)))*(bVector[i] - SumBefore(i) - SumAfter(i))

def SumBefore(i):
    sum = 0
    for j in range (i):
        if(matrix.get((i, j)) != None):
            sum += matrix.get((i,j)) * Vectorx[j]
    return sum

def SumAfter(i):
    sum = 0
    for j in range(i+1, 128, 1):
        if(matrix.get((i, j)) != None):
            sum += matrix.get((i,j)) * Vectorx[j]
    return sum

def Check(vector, vectorPrevious):
    g = 0
    for i in range (128):
        if (abs(vector[i] - vectorPrevious[i]) > 0.0000000001):
            g = 12
    return g

def GradSprzez():
    a = 0
    xk = np.array(Vectorx2)
    rk = bVector - MultiplicateVectorMatrix(xk)
    pk = np.array(rk)
    while (np.linalg.norm(rk) > 0.0000001):
        a += 1
        matrixpk = MultiplicateVectorMatrix(pk)
        RkTRk = np.dot(rk, rk)
        alpha = RkTRk / np.dot(pk, matrixpk)
        xk = np.array(xk + alpha * pk)
        rk = np.array(rk - alpha * matrixpk)
        beta = np.dot(rk, rk) / RkTRk
        pk = np.array(rk + beta * pk)
    print ("Liczba wykonanych operacji wyniosla: ")
    print (a)
    return xk

def MultiplicateVectors(vector, vector2):
    sum = 0
    for i in range (128):
        sum += vector[i] * vector2[i]
    return sum

def MultiplicateVectorMatrix(vector):
    comp = 0
    ResultVector = np.array(vector)
    for i in range (128):
        comp = 0
        for j in range(128):
            if(matrix.get((i, j)) != None):
                comp = comp + vector[j] * matrix.get((i,j))
        ResultVector[i] = comp
    return ResultVector

if (__name__ == "__main__"):
    VectorxPrevious = np.zeros(128)
    for i in range (128):
        for j in range(128):
            if (i==j):
                matrix[(i,j)] = 4.0
            if (i == j+1):
                matrix[(i,j)] = 1.0
            if (i+1 == j):
                matrix[(i,j)] = 1.0
            if (i+4 == j):
                matrix[(i,j)] = 1.0
            if (i == j+4):
                matrix[(i,j)] = 1.0
    j = 1
    a = 0
    print ("-------------------Metoda Gaussa-Seidela-------------------")
    while (bool(j)):
        a += 1
        VectorxPrevious = np.array(Vectorx)
        GaussSeidel()
        if (Check(Vectorx, VectorxPrevious) == 0):
            j = 0
    print ("Liczba wykonanych operacji wyniosla: ")
    print (a)
    print ("Wynikiem jest wektor: ")
    print (Vectorx)
    print ("---------------Metoda Gradientow Sprzezonych---------------")
    Vectorx2 = np.array(GradSprzez())
    print ("Wynikiem jest wektor: ")
    print(Vectorx2)
