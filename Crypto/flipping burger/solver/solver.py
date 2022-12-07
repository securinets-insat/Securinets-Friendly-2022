from Crypto.Util.number import long_to_bytes,bytes_to_long
from Crypto.Cipher import  AES
from Crypto.Util.Padding import pad, unpad
from pwn import *
def xorbytes(a,b):
    res=b""
    for a,b in zip(a,b):
        res+=long_to_bytes(a^b)
    return res
host="20.171.17.211"
port=6018
io=remote(host,port)
io.recvuntil(b"me : ")
enc=bytes.fromhex(io.recvline().decode())
iv=enc[:16]
enc_text=enc[16:]
print(iv)
print(enc_text)
known_text=pad(b"normal Burger",16)
target=pad(b"krabby patty",16)
new_iv=xorbytes(xorbytes(target,known_text),iv)
payload=new_iv+enc_text
io.sendline(payload.hex().encode())
io.recv()
print(io.recv())