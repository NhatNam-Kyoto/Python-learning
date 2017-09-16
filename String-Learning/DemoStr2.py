#Toán tử chuỗi: +, *
strA = "Hello"
strB = "Nhatnam-Kyoto"
strC = 'K'
strD = "H"
print(strA + " " + strB)
print(strA * 5)
#==============================
#check if strA in strB:> T or F return
print(strC in strA)
print(strD in strA)
#==============================
#Index of string: 0 > len(str) - 1; -1>>>
print(len(strA))
print(strA[0])
print(strA[len(strA) - 1])
#=============================
#Cut string: [x:y<:z>]>> cut string from x to y-1, <step z>, index di tu 0
print(strA[1:4])
print(strA[:])
print(strA[None:None])
print(strA[1:len(strA)])
print(strA[-2:])
print(strB[1:8:2])
print(strB[-2:8:-2])
#=============================
#Ep kiểu dữ liệu: dùng hàm str, int, float.... tùy vào kiểu dữ liệu ép
#Change char in string
#Python doesn't use str[x] = char, so we use another way: cut and plus string. A String in Python = hash
print(hash(strA))
strE = strA[:2] + 'K' + strA[3:]
print(strE)