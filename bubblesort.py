#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swaps = 0
    pos = len(a)
    
    for x in range(pos):
        for y in range(pos-1):
            if (a[y]> a[y+1]):
                temp = a[y]
                a[y] = a[y+1]
                a[y+1] = temp
                swaps += 1
                
                

    print("Array is sorted in " +str(swaps)+ " swaps")
    print("First Element:" + str(a[0]))
    print("Last element:" + str(a[pos-1]))
                
            
        
    
            

    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
