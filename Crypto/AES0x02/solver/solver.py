from Crypto.Util.number import  long_to_bytes,bytes_to_long

xor = lambda a,b: bytes(_a^_b for _a,_b in zip(a,b))
# xor from layka_ with love :3
msg=b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum tristique elit mattis velit tincidunt luctus. Nam vulputate suscipit lectus quis dapibus"
encryEncrypted_Flag=bytes.fromhex("eadf4e08cd37fc069abed645369c1224c36180d02f12e1a209fee4b7d869220f328740ed6b4da7bab26e2aa23ffceb0aac980322aee246124e460d66dc9dd8df1d")[16:]
Encrypted_msg=bytes.fromhex("eadf4e08cd37fc069abed645369c1224dc6b91c0305be6b70ef8f2a6e372260f35c05bb340198e96e0456ff403feb638a7af282e94a6037b6e133b608182cef30ee16f4051306fc94a0008e44fefe0ed7a49597ba8f82d6ba1b61e8c72de78aae4e79f22224dfa8be14ea67196fcd99c982a16d66bf7f3a0427e4c0b9808cb634ee32487814bad6f7969fa5551d8eaa3422b98ead40972773f94aa124d86c34331416d7486aa9bf10d7aa131")[16:]

print(xor(encryEncrypted_Flag,xor(msg,Encrypted_msg)))