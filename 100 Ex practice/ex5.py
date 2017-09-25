import math
inp = input('Nhap vo di: ')
l = inp.split(',')
resulf = []
c = 50 
h = 30
for d in l:
	resulf.append(str(round(math.sqrt(2*c*float(d)/h))))
print (','.join(resulf))
