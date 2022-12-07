from Crypto.Cipher import AES


def decrypt(ciphertext:bytes,key:bytes):

    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext
key=b"key are free tdy"

Encrypted_FLAG=bytes.fromhex("35455ce8e11dced0fd67783cb525e19a073222c5997fb36ce423b9a29fbc76c4f9ed9a8012ae19ba019dbf64d22e47893556e7895d77fd9650106e4479625eba")
print(decrypt(Encrypted_FLAG,key))