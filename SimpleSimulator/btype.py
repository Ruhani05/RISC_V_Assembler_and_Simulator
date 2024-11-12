def binary_to_decimal(binary):
    if binary[0] == '1':
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary)
        inverted_decimal = int(inverted_binary, 2) + 1
        decimal = -inverted_decimal
    else:
        decimal = int(binary, 2)
    return decimal
def binary_to_decimal_unsigned(binary):
    decimal_value = int(binary, 2)
    return decimal_value
def beq(s,d,pc):
    if (binary_to_decimal(d[s[7:12]]))==(binary_to_decimal(d[s[12:17]])):
        pc=pc+binary_to_decimal(s[0]+s[24]+s[1:7]+s[20:24]+'0')
    else:
        pc=pc+4
    return pc
def bne(s,d,pc):
    if (binary_to_decimal(d[s[7:12]]))!=(binary_to_decimal(d[s[12:17]])):
        pc=pc+binary_to_decimal(s[0]+s[24]+s[1:7]+s[20:24]+'0')
    else:
        pc=pc+4
    return pc
def bge(s,d,pc):
    if (binary_to_decimal(d[s[7:12]]))<(binary_to_decimal(d[s[12:17]])):
        pc=pc+binary_to_decimal(s[0]+s[24]+s[1:7]+s[20:24]+'0')
    else:
        pc=pc+4
    return pc
def bgeu(s,d,pc):
    if (binary_to_decimal_unsigned(d[s[7:12]]))<(binary_to_decimal_unsigned(d[s[12:17]])):
        pc=pc+binary_to_decimal(s[0]+s[24]+s[1:7]+s[20:24]+'0')
    else:
        pc=pc+4
    return pc
def blt(s,d,pc):
    if (binary_to_decimal(d[s[7:12]]))>(binary_to_decimal(d[s[12:17]])):
        pc=pc+binary_to_decimal(s[0]+s[24]+s[1:7]+s[20:24]+'0')
    else:
        pc=pc+4
    return pc
def bltu(s,d,pc):
    if (binary_to_decimal_unsigned(d[s[7:12]]))>(binary_to_decimal_unsigned(d[s[12:17]])):
        pc=pc+binary_to_decimal(s[0]+s[24]+s[1:7]+s[20:24]+'0')
    else:
        pc=pc+4
    return pc
def check(s,d,pc):
    if s[17:20] == "000":
       return beq(s,d,pc)
    elif s[17:20] == "001":
       return bne(s,d,pc)
    elif s[17:20] == "100":
       return blt(s,d,pc)
    elif s[17:20] == "101":
       return bge(s,d,pc)
    elif s[17:20] == "110":
       return bltu(s,d,pc)
    elif s[17:20] == "111":
       return bgeu(s,d,pc)
    else:
        return pc
