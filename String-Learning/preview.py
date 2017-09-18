str1 = "Xin chào"
str2 = "Nhatnam-Kyoto"
str3 = "Lacthan"

'''note test '''
print(str1 + " " +str2)
print((str1 + "-") *5)
print("K" in str1)
print("X" in str1)
print(len(str3))
for x in range(len(str3)):
	print ('str3 [' + str(x) + ']= ' + str3[x])

print(str3[1:3])
print(str3[0:7:2])
print(str3[-4:-1])
print(str3[4:-1])

str4 = str2[None:8] + str3
print(str4)
print(type(str4))
print(hash(str2))