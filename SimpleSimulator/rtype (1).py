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

def bd(binary):
    if binary[0] == '1':
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary)
        inverted_decimal = int(inverted_binary, 2) + 1
        decimal = -inverted_decimal
    else:
        decimal = int(binary, 2)

    return decimal

def bidu(binary):
    return int(binary, 2)
   
def add(s, d):
    d[s[20:25]]=db(bd(d[s[12:17]])+bd(d[s[7:12]]))
    
    return d

def sub(s, d):
    d[s[20:25]]=db(bd(d[s[12:17]])-bd(d[s[7:12]]))
    return d 

def sll(s, d):
    d[s[20:25]]=(db(bd(d[s[12:17]])<<(bidu((d[s[7:12]])[27:32]))))[-32:]
    return d

def slt(s, d):
    if bd(d[s[12:17]])<bd(d[s[7:12]]):
        d[s[20:25]]=db(1)
    return d

def sltu(s, d):
    if bidu(d[s[12:17]])<bidu(d[s[7:12]]):
        d[s[20:25]]=db(1)
    return d

def xor(s, d):
    d[s[20:25]]=db(bd(s[12:17])^bd(s[7:12]))
    return d

def srl(s, d):
    d[s[20:25]]=db(bd(d[s[12:17]])>>bidu(d[s[7:12]][27:32]))[:32]
    return d

def ory(s, d):
    d[s[20:25]]=db(bd(d[s[12:17]])|bd(d[s[7:12]]))
    return d

def andy(s, d):
    d[s[20:25]]=db(bd(d[s[12:17]])&bd(d[s[7:12]]))
    return d

def mul(s, d):
    d[s[20:25]]=db(bd(d[s[12:17]])*bd(d[s[7:12]]))
    return d

def check(s, d):
    if s[17:20]=="000" and s[0:7]=="0000000":
        d=add(s, d)
    elif s[17:20]=="000" and s[0:7]=="0100000":
        d=sub(s, d)
    elif s[17:20]=="001" and s[0:7]=="1111111":
        d=mul(s, d)
    elif s[17:20]=="001" and s[0:7]=="0000000":
        d=sll(s, d)
    elif s[17:20]=="010":
        d=slt(s, d)
    elif s[17:20]=="011":
        d=sltu(s, d)
    elif s[17:20]=="100":
        d=xor(s, d)
    elif s[17:20]=="101":
        d=srl(s, d)
    elif s[17:20]=="110":
        d=ory(s, d)
    elif s[17:20]=="111":
        d=andy(s, d)
    return d
