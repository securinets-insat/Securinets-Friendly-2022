from Crypto.Cipher import AES
from Crypto.Util import  Counter
from Crypto.Util.number import  long_to_bytes,bytes_to_long
import os
KEY=os.urandom(16)
IV=bytes_to_long(os.urandom(16))
def encrypt(plaintext):
    cipher = AES.new(KEY, AES.MODE_CTR, counter=Counter.new(128, initial_value=IV))
    encrypted = cipher.encrypt(plaintext)
    return (long_to_bytes(IV)+encrypted).hex()

flag=open("flag.txt","rb").read()
msg=b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum tristique elit mattis velit tincidunt luctus. Nam vulputate suscipit lectus quis dapibus"
print(f"Encrypted Flag: {encrypt(flag)}")
print(f"Encrypted msg: {encrypt(msg)}")
