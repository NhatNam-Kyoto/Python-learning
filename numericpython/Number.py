#Number in Python: interger, float, fraction, complex.
# interger: không giới hạn độ lớn
inte = 17
print(inte)
# in ra kiểu dữ liệu của vari..
print(type(inte))
#===================================================
#float: số thực
flo = 6.9
print(flo)
print(type(flo))
#số thực trên python giới hạn bới 15 chữ số phần thập phân: ex
flo2 = 6.12345678910111213
print(flo2)

#Ta dùng thư viện decimal để dùng trên 15 số;
# import Decimal libary; dấu *>> dùng toàn bộ thư viện
from decimal import*
# Set số chữ số dùng getcontext()., mặc định là 30
#getcontext().prec = 20
sub = Decimal(10)/3
print(sub)
print(type(sub))
#========================================
#fraction: phân số
#Khai báo: import thư viện: fraction, hàm fraction(tử,mẫu)
from fractions import*
fra = Fraction(6,9)
fra1 = Fraction(5,6)
print(fra)
print(type(fra))
print(fra + fra1)
#========================================
#số phức: a+bj
#Khai báo: hàm: complex(phần thực, phần ảo)
com = complex(4, 5)
print(com)
print(type(com))