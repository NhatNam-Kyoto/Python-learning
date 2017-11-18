

import re

stg = 'AT is real. So Kyoto will catch her!!! AT_1s_R34l'
pattern = 'AT'
#==================================================================================================
print r'----------------re.match(pattern, stg, [flag] = 0) =>>>> Object----------------------------'
print r'----------------re.fullmatch(pattern, stg, [flag] = 0) (so sanh hoan toan) =>>>> Object----------------------------'
match_1 = re.match(pattern,stg)
match_1_1 = re.match(pattern,stg,1)

print match_1_1
print match_1
if match_1:
	print "AT found!"
else:
	print "AT not found"
'''match_2 = re.fullmatch(pattern,stg)
if match_2:
	print "AT found!"
else:
	print "Not found"'''
#==================================================================================================
print r'---------------match(search...).group([index] = 0) =>>>> List-----------------------------'
print re.search(r'AT', stg).group()
print 'Match found: ' + match_1_1.group() + '- iNDEX: ' + str(match_1_1.group().index(match_1_1.group()))


#==================================================================================================
print r'---------------match(search...).groups() =>>>> tuple-----------------------------'
print re.search(r'(.*) AT',stg).groups()


#==================================================================================================
print r'----------------re.search(pattern, stg, [flag] = 0) =>>>> ----------------------------'
se = re.search('4T',stg)
if se:
	print se.groups()
else:
	print '4T not found!!'

#==================================================================================================
print r'----------------re.split(pattern, string, maxsplit) =>>> so khop va cat chuoi so khop thanh cong'
print re.split(pattern, stg)
print re.split(pattern, stg, 2)


#==================================================================================================
print r'----------------findall(partern, string, flags) =>>> list-------------------------------'
print re.findall(pattern,stg)


#==================================================================================================
print r'---------------sub(pattern, replace, string, flags) =>>> tim va thay the----------------'
print re.sub(pattern,'4T',stg)


#==================================================================================================

print r'---------------pattern syntax-----------------------------------------------------------'
if re.match(r'[A-Z]',stg):
	print "Khop: " + str(re.match(r'[A-Z]',stg))
else:
	print "Khong khop"

#==================================================================================================
if re.match(r'[4y]',stg):
	print "Khop: " + str(re.match(r'[4y]',stg))
else:
	print "Khong khop"

#=========================================^s =>> s co phai la dau chuoi============================
if re.search(r'^A',stg):
	print "Khop: " + str(re.search(r'^A',stg))
else:
	print "Khong khop"

if re.search(r'^t',stg):
	print "Khop: " + str(re.search(r'^t',stg))
else:
	print "Khong khop"

#========================================s$ =>> s co phai la cuoi chuoi============================
if re.search(r'l$',stg):
	print "Khop: " + str(re.search(r'l$',stg))
else:
	print "Khong khop"

if re.search(r'r$',stg):
	print "Khop: " + str(re.search(r'r$',stg))
else:
	print "Khong khop"

#=======================================
print 'Thoi toi day met roi, ghi ra txt cho le :)'
