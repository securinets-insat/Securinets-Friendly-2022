from Crypto.Cipher import AES
def encrypt(plaintext:bytes,key:bytes):
    if len(plaintext) % 16 != 0:
        return {"error": "Data length must be multiple of 16"}

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(plaintext)
    return encrypted
key=b"key are free tdy"

flag=open("flag.txt","rb").read()
len(flag)%16

def decrypt(ciphertext:bytes,key:bytes):

    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext
key=b"key are free tdy"
print(f'Encrypted FLAG: {encrypt(flag,key).hex()}')

#Encrypted FLAG: 35455ce8e11dced0fd67783cb525e19a073222c5997fb36ce423b9a29fbc76c4f9ed9a8012ae19ba019dbf64d22e47893556e7895d77fd9650106e4479625eba

