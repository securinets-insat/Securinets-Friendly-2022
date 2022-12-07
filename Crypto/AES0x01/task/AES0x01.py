from Crypto.Cipher import AES
# urandom generate  random bytes
from os import  urandom

def encrypt(plaintext:bytes,key:bytes):
    if len(plaintext) % 16 != 0:
        return {"error": "Data length must be multiple of 16"}
    IV=urandom(16)
    cipher = AES.new(key, AES.MODE_CBC,IV)
    encrypted = cipher.encrypt(plaintext)
    return IV+encrypted
flag=b"here's your flag: ??????????????????????????????????????????"

key=flag[:16]
print(f"Encrypted flag: {encrypt(flag,key).hex()}")


#Encrypted flag: abe907665fe3f61cc62e463bef10392e4dcdb5343e844f63a6b9399ca4597483d3380e098286d6d69d6d26a085548ee8662c0328390546b8292bba5c82b0d3a4c6c124209a815565c1d19259259a67cd5c4163253ac4861a5920500f1f446b13
