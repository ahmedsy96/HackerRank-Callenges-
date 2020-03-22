# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:54:19 2020

@author: jadee
"""

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    d=list(s)
    count =0
    for i in range(len(d)):
        if d[i] == 'a':
            count+=1
    k = int((n / len(d))) * count 
    if n % len(d) == 0 : 
        return(k)
    else : 
        l = 0
        for i in range (n%len(d)): 
            if d[i]=='a': 
                l+=1
        return(k+l)
