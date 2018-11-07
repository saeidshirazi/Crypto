from Crypto.Cipher import AES
import random, string, base64
##########
#Using pycrypto
##########
key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(32))
iv = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))

print(key, len(key))
print(iv, len(iv))

enc_s = AES.new(key, AES.MODE_CFB, iv)
cipher_text = enc_s.encrypt('1')
encoded_cipher_text = base64.b64encode(cipher_text)
print(encoded_cipher_text)