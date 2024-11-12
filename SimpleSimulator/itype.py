def bd(binary):
    if binary[0] == '1':
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary)
        inverted_decimal = int(inverted_binary, 2) + 1
        decimal = -inverted_decimal
    else:
        decimal = int(binary, 2)
    return decimal

def db(decimal_num):
    if decimal_num < 0:
        abs_decimal = abs(decimal_num)
        complement = 2**32 - abs_decimal
    else:
        complement = decimal_num

    twos = bin(complement)[2:]
    
    if len(twos) < 32:
        twos = '0' * (32 - len(twos)) + twos
    return twos

def bidu(binary):
    return int(binary, 2)

def decimal_to_hexadecimal(decimal_num):
    hexnum = hex(decimal_num)
    hexnum = hexnum[2:]
    hexnum = hexnum.zfill(8)
    hexnum = '0x' + hexnum
    return hexnum

def lw(s,d,datamem, pc):
    imm=s[-32:-20]
    mem=decimal_to_hexadecimal(bd(d[s[12:17]])+(bd(imm)))
    d[s[-12:-7]]=datamem[mem]
    return d

def addi(s,d, pc):
    imm=s[-32:-20]
    d[s[-12:-7]]=db(bd(d[s[-20:-15]])+bd(imm))
    return d

def sltiu(s,d, pc):
    if bidu(d[s[-20:-15]])<bidu(s[-32:-20]):
        d[s[19:24]]=db(1)
    return d

def jalr(s,d,pc):
    imm=20*s[0]+s[-32:-20]
    d[s[-12:-7:]]= db(pc + 4)
    pc=(bd(d[s[-20:-15]])+bd(imm))
    x=db(pc)
    y=x[:-1]+'0'
    pc=bd(y)
    return d, pc
    
def check(s,d,pc,datamem):
    if s[17:20] == "010":
        return lw(s,d,datamem, pc)
    elif s[17:20] == "000" and s[25:32]!="1100111":
        return addi(s, d, pc)
    elif s[17:20] == "011":
       return sltiu(s,d, pc)
    elif s[17:20] == "000" and s[25:32]=="1100111":
       return jalr(s,d,pc)
