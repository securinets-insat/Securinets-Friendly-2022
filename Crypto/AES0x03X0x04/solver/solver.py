#this is only for the part 1 the second one is the same thinni :3
from pwn import *
import json
from string import printable

host = '20.171.17.211'
port = 7001
io = remote(host, port)
print(io.recv())
Flag=b""

def ret_json(input):
  json_payload={}
  json_payload["option"]="1"
  json_payload["msg"]=payload.hex()
  return json.dumps(json_payload)



def parse_json(jsondata):
  data=bytes.fromhex(json.loads(jsondata.decode())["encrypted_msg"])
  return data[16*2:16*3]

for i in range(1,40):

  payload=b"0"*(16*3-len(Flag)-1)
  io.sendline(ret_json(payload).encode())
  target=parse_json(io.recv())
  for j in printable:

    payload=b"0"*(16*3-len(Flag)-1)+Flag+j.encode()
    io.sendline(ret_json(payload).encode())
    trial=parse_json(io.recv())
    
    if trial == target:
      Flag+=j.encode()

      print(Flag)
      break

print(Flag)