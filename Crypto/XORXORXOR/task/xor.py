from Crypto.Util.number import long_to_bytes

key=open("key.txt","rb").read()
assert len(key)==12

flag=open("flag.txt").read()
assert len(flag)==96

def xor(plainetext,key):
    ciphertext=b""
    for i in range(len(plainetext)):
        ciphertext+=long_to_bytes(plainetext[i]^key[(i)%len(key)])
    return ciphertext.hex()

print(f"ciphertext :{xor(flag,key)}")
# ciphertext :0b0a113e17101c00171c0d79683d2d2056002d37500c46773d3d0b140c5d2d56023c2f7e3e59417b04184256025c4f143a59162f564c1406570e13406a58442f034a4a54065e14193a5f427c554d4a50025c44186009117f524e4155015f4f5c