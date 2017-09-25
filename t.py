cipher = "\jp%bjq%wlbmq%n`|)%gpq%Sdh%lv%hlk`%?A%Qjj%idq`$$"
plaintext = ""

for i in range(len(cipher)):
   plaintext += str(ord(cipher[i]) ^ 5)

print (bin(int(plaintext)))