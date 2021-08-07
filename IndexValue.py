import numpy as np
import math

"""
this is program to calculate
1. Lespeyres index
2. Paasche Index
3. Fisher's Ideal index
4. Value Index
"""

"""
notes :
pt is the current price
p0 is the price in the base period
qt is the quantity in the current period
q0 is the quantity in the base period
"""

#fill the array with value you want to calculate
p0 = np.array([0.77,1.85,0.88,1.46,1.58,4.40])
pt = np.array([0.89,1.84,1.01,1.56,1.70,4.52])
q0 = np.array([50,26,102,30,40,12])
qt = np.array([55,20,130,40,41,12])

ptq0 = sum(pt * q0)
p0q0 = sum(p0 * q0)
ptqt = sum(pt * qt)
p0qt = sum(p0 * qt)


#lespeyres index
def lespeyres(a,b):
       return a / b * 100

#paasche index
def paasche(c,d):
       return c / d * 100
       
#fisher's ideal index
def fisher(e,f):
       j = e * f
       return math.sqrt(j)
       
#value index
def vIndex(g, h):
       return g / h * 100

lespIndex = lespeyres(ptq0,p0q0)
paasIndex = paasche(ptqt,p0qt)
fisherIdealindex = fisher(lespIndex, paasIndex)
valueIndex = vIndex(ptqt, p0q0)

print(round(lespIndex, 2))
print(round(paasIndex, 2))
print(round(fisherIdealindex, 2))
print(round(valueIndex, 2))



