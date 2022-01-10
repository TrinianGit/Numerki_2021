#!/usr/bin/env python

import numpy as np
import argparse
import sys

def addRow(row , mul):
    size = (len(mul) , len(mul))
    l = np.zeros(size)
    for i in range(size[0]):
        l[i , i] = 1.0
    for i in range(size[0]):
        l[i , row] += mul[i]
    return l

def mulRow(mul):
    return np.diag(mul)

def permuteMatrix(row, row2, size):
    matsize = (size, size)
    per = np.zeros(matsize)
    per[row, row2] = 1
    per[row2, row] = 1
    for i in range(matsize[0]):
        if (i != row and i != row2):
            per[i, i] = 1;
    return per

def nicePrint(m , description = None):
    shape = m.shape
    mStr = [[str(round(m[r , c], 8)) for c in range(shape[1])] for r in range(shape[0])]

    maxLen = 0
    for r in range(shape[0]):
        for c in range(shape[1]):
            if(len(mStr[r][c]) > maxLen):
                maxLen = len(mStr[r][c])

    if(not description is None):
        sys.stdout.write(description)

    for r in range(shape[0]):
        if(not description is None):
            if(r != 0):
                sys.stdout.write(" " * len(description))
        sys.stdout.write("[ ")
        for c in range(shape[1]):
            sys.stdout.write(mStr[r][c] + " " * (maxLen - len(mStr[r][c]) + 1))
        sys.stdout.write("]\n")
    sys.stdout.write("\n")

if(__name__ == "__main__"):
    parser = argparse.ArgumentParser(description = "Manipulate matrix.")
    parser.add_argument("matrix" , help = "Matrix entered following the format example: 1 2 3 , 4 5 6 , 7 8 9")
    args = parser.parse_args()
    
    a = np.array(list(map(lambda r : list(map(float , r.split())) , args.matrix.split(','))))
    nicePrint(a , description = "A = ")
    # rectangular matrix check TODO
    p = np.identity(a.shape[0])
    b = np.copy(a)
    m = np.identity(a.shape[0])
    mInv = np.identity(a.shape[0])

    con = True
    while(con):
        command = input(
                "Enter command:\n"
                "    add <row from> <row to> <mul>\n"
                "    mul <row> <mul>\n"
                "    div <row> <mul>\n"
                "    per <row> <row>\n"
                "    quit\n"
                )
        per = None
        mod = None
        modInv = None
        if(len(command.split()) == 4 and command.split()[0] == "add"):
            rowFrom = int(command.split()[1]) - 1
            rowTo = int(command.split()[2]) - 1
            mul = float(command.split()[3])
            mod = addRow(rowFrom , [(mul if r == rowTo else 0.0) for r in range(a.shape[0])])
            modInv = addRow(rowFrom , [(-mul if r == rowTo else 0.0) for r in range(a.shape[0])])
            nicePrint(mod , "<adding row multiple> = ")
            nicePrint(modInv , "<adding row multiple>^-1 = ")
        elif(len(command.split()) == 3 and command.split()[0] == "mul"):
            row = int(command.split()[1]) - 1
            mul = float(command.split()[2])
            mod = mulRow([(mul if r == row else 1.0) for r in range(a.shape[0])])
            modInv = mulRow([((1.0 / mul) if r == row else 1.0) for r in range(a.shape[0])])
            nicePrint(mod , "<multiplying row> = ")
            nicePrint(modInv , "<multiplying row>^-1 = ")
        elif(len(command.split()) == 3 and command.split()[0] == "div"):
            row = int(command.split()[1]) - 1
            mul = float(command.split()[2])
            mod = mulRow([((1.0 / mul) if r == row else 1.0) for r in range(a.shape[0])])
            modInv = mulRow([(mul if r == row else 1.0) for r in range(a.shape[0])])
            nicePrint(mod , "<multiplying row> = ")
            nicePrint(modInv , "<multiplying row>^-1 = ")
        elif(len(command.split()) == 3 and command.split()[0] == "per"):
            first_row = int(command.split()[1]) - 1
            second_row = int(command.split()[2]) - 1
            per = permuteMatrix(first_row, second_row, a.shape[0])
        elif(command == "quit"):
            con = False
        if (not per is None):
            b = np.matmul(per, b)
            p = np.matmul(per, p)
            nicePrint(p, "P = ")
            nicePrint(a, "A = ")
            nicePrint(b, "B = ")
        elif(not mod is None):
            m = np.matmul(mod , m)
            mInv = np.matmul(mInv , modInv)
            b = np.matmul(mod , b)
            print("\n\nM . A = B")
            nicePrint(m , description = "M = ")
            nicePrint(a , description = "A = ")
            nicePrint(b , description = "B = ")
            print("\n\nP . A = M^-1 . B")
            nicePrint(p, description = "P = ")
            nicePrint(mInv , description = "M^-1 = ")
    print("\n\nM^-1 . B = P . A")
    nicePrint(np.matmul(mInv , b) , description = "M^-1 . B = ")
    nicePrint(np.matmul(p, a) ,     description = "P . A    = ")
    nicePrint(a ,     description = "A        = ")
