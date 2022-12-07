from sympy import  legendre_symbol
from Crypto.Util.number import  bytes_to_long
from random import  randint

p=59251020809286681364606559971771455720703275930550785469089134515250431707559
x=2

assert legendre_symbol(x,p)==1
flag=open("flag.txt","rb").read()
plainbin=bin(bytes_to_long(flag))[2:]
ciphertext=[]
for i in plainbin:
    if i =="1":
        ciphertext.append((pow(randint(2,p),3,p)*x)%p)
    else:
        ciphertext.append(pow(randint(2,p),3,p))
print(ciphertext)
