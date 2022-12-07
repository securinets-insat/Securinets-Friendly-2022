from Crypto.Cipher import AES
def decrypt(plaintext,key,IV):

    cipher = AES.new(key, AES.MODE_CBC,IV)
    encrypted = cipher.decrypt(plaintext)
    return encrypted
Encrypted_flag=bytes.fromhex("abe907665fe3f61cc62e463bef10392e4dcdb5343e844f63a6b9399ca4597483d3380e098286d6d69d6d26a085548ee8662c0328390546b8292bba5c82b0d3a4c6c124209a815565c1d19259259a67cd5c4163253ac4861a5920500f1f446b13")

key=b"here's your flag"
IV=Encrypted_flag[:16]
Encrypted_flag=Encrypted_flag[16:]
print(decrypt(Encrypted_flag,key,IV))