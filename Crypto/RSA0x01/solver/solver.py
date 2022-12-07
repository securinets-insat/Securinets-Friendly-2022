from Crypto.Util.number import long_to_bytes
pubkey= 56093991873348435075537312549220979223753524001395993888906045240875257794029
p= 263068581345753191476848934394284602217
q= 213229537280332393794037487968778136037
e= 65537
d= 26767833465784197606731371784859497752853685128366359648563192652854881794625
ciphertext= 23200768492072682493016235461786292103914622615318283632579188917099680136324
print(long_to_bytes(pow(ciphertext,d,pubkey)))