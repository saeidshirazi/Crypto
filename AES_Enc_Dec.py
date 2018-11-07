from Crypto.Cipher import AES
import random, string, base64
##########
#Using pycrypto
##########
key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(32))
iv = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))
print('key is:',key,'\nkey length is:', len(key))
print('############################################################')
print('IV is:',iv,'\nIV lenght is:', len(iv))
print('############################################################')
def enc():
    enc_s = AES.new(key, AES.MODE_CFB, iv)
    get_text_from_user = input('please enter yopur msg: ')
    cipher_text = enc_s.encrypt(get_text_from_user)
    encoded_cipher_text = base64.b64encode(cipher_text)
    print('cipher text is:',encoded_cipher_text)
    return encoded_cipher_text

#enc()

def decrypt():
    dec_msg=enc()
    decryption_suite = AES.new(key, AES.MODE_CFB, iv)
    plain_text = decryption_suite.decrypt(base64.b64decode(dec_msg))
    print('############################################################')  
    print('plain text is:',plain_text)

decrypt()

