#Hàm không có giá trị trả về
def xinchao(ten):
	print('xin chao: ' + ten)
xinchao('Nam')
#Hàm có giá trị trả về: return,các dòng lệnh sau return cũng sẽ không được thực thi
def add(num1, num2):
	print(num1, "+", num2,'= ',num1 + num2)
	return num1+num2
	print('tao lao thien tac')
x = add(4,6)
print (x)
#thêm một số không xác định giá trị vào ham, dùng *var: tupple
def add1(num1,*num2):
	for x in num2:
		num1 += x
	print(num1)
	return num1
test = add1(1,2,3,4,5,6,7,8)
print(test)