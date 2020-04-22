# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:59:27 2020

@author: jadee
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    
    myhourglasses= []
    for i in range(4): # i is row index
        for j in range (1,5): #j is column index
            myhourglasses.append(arr[i][j-1] 
            + arr[i][j]
            +arr[i][j+1]
            +arr[i+1][j]
            +arr[i+2][j-1]
            +arr[i+2][j]
            +arr[i+2][j+1])
    return (max(myhourglasses))
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    #print(arr[5][5])
    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
