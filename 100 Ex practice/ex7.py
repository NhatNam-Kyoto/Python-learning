'''Write a program which takes 2 digits, X,Y
as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
'''
def multi(x,y):
	resulf = [[y*x for y in range(y)] for x in range (x)]
	return resulf
def nhap(inp):
	arr = [int(x) for x in inp.split(',')]
	return arr
inp = input('Nhap vao: ')
arr = nhap(inp)
x = arr[0]
y = arr[1]
print(multi(x,y))
