from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from os import  urandom
import json


key=urandom(16)


FLAG_1=open("flag_1.txt","rb").read()
FLAG_2=open("flag_2.txt","rb").read()

banner=""""
   ________  _____    __________  ___    __
  / ____/ / / /   |  / ____/ __ \/   |  / /
 / /   / /_/ / /| | / /_  / /_/ / /| | / / 
/ /___/ __  / ___ |/ __/ / _, _/ ___ |/_/  
\____/_/ /_/_/  |_/_/   /_/ |_/_/  |_(_)   
                                           """
def Aes_encrypt_1(msg):
    plaintext=msg+FLAG_1
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext,16))
    return ciphertext



def Aes_encrypt_2(IV):
    plaintext="".join(i*16 for i in FLAG_2).encode()
    cipher = AES.new(key, AES.MODE_CBC,IV)
    ciphertext = cipher.encrypt(plaintext,16)
    return ciphertext.hex()


  
def encrypt():
    your_input=json.loads(input())

    if "option" not in your_input:
         return {"error":"You need to send me an option"}

    if "msg" not in your_input:
        return{"error":"You need to send me a message to encrypt"}

    if your_input["option"]=="1":
        your_msg=bytes.fromhex(your_input["msg"])
        plaintext=your_msg+FLAG_1
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(plaintext,16))
        return json.dumps({"encrypted_msg":ciphertext.hex()})


    elif your_input["option"]=="2":
        your_msg=bytes.fromhex(your_input["msg"])
        if(len(your_msg)!=16):
            return{"error":"IV need a specifi lenght"}

        encrypt_flag=Aes_encrypt_2(your_msg)
        return json.dumps({"encrypted_msg":encrypt_flag.hex()})

    else:
        return {"error":"Your option is Not available yet!"}

print(banner)

while True:
    try:
        print(encrypt())
    except:
        print("Don't send something stupid")


