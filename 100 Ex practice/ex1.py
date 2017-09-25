'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

list1 = []
for x in range(2000,3201):
	if (x%7==0) and (x%5!=0):
		list1.append(str(x))
print(','.join(list1))
print(type(','.join(list1)))

''' str.join(sequence) function
return>>> type: string
		  nối các phần tử trong 1 seq;
		   ngăn cách bởi str("")
'''