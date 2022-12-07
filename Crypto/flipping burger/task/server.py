from os import  urandom
from time import sleep
from Crypto.Cipher import  AES
from Crypto.Util.Padding import pad, unpad
key = urandom(16)
iv = urandom(16)

flag = open("flag.txt","r").read()


def encrypt(data):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    print(data)
    enc = cipher.encrypt(pad(data,16))
    return enc.hex()

def decrypt(encryptedParams):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    paddedParams = cipher.decrypt(encryptedParams)
    return unpad(paddedParams,16)

msg = b"normal Burger"

print("Can you flip my burger for me : " + str(iv.hex()) + str(encrypt(msg)))
enc_msg=""
try:
    enc_msg = input("I will be waiting for you : ")

    iv=bytes.fromhex(enc_msg[:32])
    enc_msg=bytes.fromhex(enc_msg[32:])
    final_dec_msg = decrypt(enc_msg)

    if b"krabby patty" in final_dec_msg:
        print('its my new  favorite burger!')
        print(flag)
    else:
        print('You should quit flipping burger !!')

except:
    print("what is this abomination?!!")