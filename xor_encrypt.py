import hashlib
__copywrite__= 'undercover'
gettext= input("please enter your msg: ")
key = input("please enter your key: ")

c  = len(gettext)
ck = len(key)

cipher = ""
for i in range(c):
    t= gettext[i]
    k= key[i%ck]
    #ord=get unicode ^= xor
    x = ord(k) ^ ord(t)
    cipher +=chr(x)

print(hashlib.md5(cipher.encode('utf-8')))
