#biến Global
x = 6
def prin():
	x = 5 #local
	print(x)
prin()
print(x)

#covert local >>global
def prin1():
	global x
	x = 7
	print(x)
prin1()
print(x)