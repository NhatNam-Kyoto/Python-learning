#https://docs.python.org/3/library/mathimport .html
#import thư viện: improt. <tên thư viện>
import math
a = 6.85
b = 8
c = 4
#Một số hàm cơ bản
#syntax: <tên thư viện>.<tên hàm>
#trả về số nguyên của <x>: trunc<x>
print(math.trunc(a))

#trả về một số nguyên được làm tròn từ <x>, return <x'> <= <x>: floor(<x>)
print(math.floor(a))

#trả về một số nguyên được làm tròn từ <x>, return <x'> >= <x>: ceil(<x>)
print(math.ceil(a))

#return |x|: fabs(<x>): float
b1 = math.fabs(b)
print(b1)
print(type(b))
print(type(b1))

#return sqrt(<x>):float
print(math.sqrt(c))
print(type(math.sqrt(c)))

#return > UCLN(a,b): gcd(a,b): int