'''Tính giai thừa một số cho trước
'''
x=int(input())
y = x
# dùng hàm
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
print (fact(x))
# dùng if + while
gt = 1
if x == 0:
	print(1)
else:
	while x > 0:
		gt = gt * x
		x = x - 1
print(gt)
# dùng for
gt1 = 1
num = y
if y == 0:
	print(1)
else:
	for y in range(2,num + 1):
		gt1 = gt1 * y
		y += 1
print(gt1)
