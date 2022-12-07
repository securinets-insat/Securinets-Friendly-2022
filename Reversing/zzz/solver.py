from z3 import *


lengthFlag = 29
flag = [BitVec(f"flag{i}", 8) for i in range(0, lengthFlag)]

mine = Solver()
mine.add(Sum(flag)==2657)
mine.add((flag[26] + flag[24] +flag[15] + flag[13] + flag[4] + flag[2] + flag[0] + flag[28]) == 803)
mine.add(flag[11]^flag[12]==flag[11] ^ flag[18])
mine.add(flag[11]^flag[12]==flag[11] ^ flag[24])
mine.add(flag[14] + flag[15]==flag[16] + flag[17])
mine.add(flag[13]==119)
mine.add(flag[22]*flag[21]==flag[22]*flag[22])
mine.add(flag[14]-1==flag[21])
mine.add(flag[19]== 115)
mine.add(flag[19]+flag[23]==2*flag[19]-3)
mine.add(flag[29-4]-flag[29-3]==flag[29-4]-flag[29-4])
mine.add((flag[29-4]-flag[29-3]==flag[29-4]-flag[29-4]))
mine.add(flag[29-3]==flag[29-2])
mine.add(flag[2]*flag[3]==5695)
mine.add(flag[2]^flag[3]==(flag[4]^flag[5])-5)
mine.add(flag[4]^flag[5]^flag[6] == 85)
mine.add(flag[6]^flag[7]^flag[8]==95)
mine.add((flag[8]+flag[9]+flag[10])==((flag[10]^flag[11]^flag[12])+(flag[12]^flag[13]^flag[14])+19)*2+42)
mine.add((((flag[17]^flag[18]^flag[19])+flag[1])+17)==flag[16]^flag[15]^flag[16])
mine.add(flag[19]+flag[20]==223)
mine.add(flag[0]==83)
mine.add(flag[1]==69)
mine.add(flag[2]==67)
mine.add(flag[10]==123)
mine.add(flag[20]-8==100)
mine.add((flag[28]+flag[0]-8)==(flag[27]+flag[1]+9))
mine.add(flag[26]+flag[25]+flag[0]-27==flag[25]+flag[24]+flag[0])
mine.add(flag[23]+flag[24]-flag[22]-flag[21]-flag[20]==-3)
mine.add(flag[22]-flag[21]+flag[20]-flag[19]== -7)
mine.add(flag[4]+flag[5]==155)
mine.add(flag[5]+flag[6]==151)
mine.add(flag[6]+flag[7]==147)
mine.add(flag[11]+flag[12]+6==flag[10]+flag[9])
mine.add(flag[9]+flag[12]-7== flag[13]+flag[14])

if mine.check() == sat:
	m = mine.model()
	print(m)

