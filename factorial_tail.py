"""
Returns amount of zeores in the end of number factorial
"""

from math import *

def zeroes (base, number):
    zeros = number
    j = base
    for i in range(2,base+1):
        if j%i == 0:
            p = 0
            while j%i == 0:
                p+=1
                j/=i
            c=0
            k=number
            while k/i > 0:
                c+=k/i
                k/=i
            zeros = min(zeros,c/p)
    return int(zeros)
