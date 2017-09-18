from decimal import *
from fractions import *
import math
getcontext().prec = 30
print(type(4+5))
print(type(4.0+5))
print(Decimal(10)/3)
print(type(Decimal(10)/3))
ps = Fraction(4,5)
print(ps)
print(type(ps))
sp = complex(4,5)
print(sp)
print(type(sp))
print('PT: ' + str(sp.real) + ' - PA: ' +str(sp.imag))
print(15 // -4)
print(math.trunc(15/-4))
