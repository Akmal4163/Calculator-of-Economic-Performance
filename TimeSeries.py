import numpy as np
import math

ns = np.array([17.5,19,21,22.7,24.5,26.7,27.3])
t = np.array([1,2,3,4,5,6,7])

nst = ns * t
tk = t * t
sumns = sum(ns)
sumt = sum(t)
sumnst = sum(nst)
sumtk = sum(tk)
def sumofb(sumnst, sumt, sumtk, sumns):
    return sumnst - sumns * sumt / 7 /sumtk - (sumt * sumt)/7

b = sumofb(sumnst, sumt,sumtk,sumns)

def sumofa(sumns, b, sumt):
    return (sumns / 7) - b * (sumt / 7)
    
a = sumofa(sumns, b, sumt)
print(a)

def yhat(a, b, j):
    return a + b * j
    
result = yhat(a, b, 9)
print(result)
