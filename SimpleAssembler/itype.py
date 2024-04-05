def decimal_to_twos_complement_12(decimal_num):
    if decimal_num < 0:
        abs_decimal = abs(decimal_num)
        complement = 2**12 - abs_decimal
    else:
        complement = decimal_num

    twos = bin(complement)[2:]
    
    if len(twos) < 12:
        twos = '0' * (12 - len(twos)) + twos
    
    return twos

    
def lw(l,d):
    if int(l[2])==-2**11:
            return decimal_to_twos_complement_12(int(l[2])) + d[l[3].rstrip(")")] + "010" + d[l[1]] + "0000011"

    if abs(int(l[2]))>=2**11:
        return "0"
    return decimal_to_twos_complement_12(int(l[2])) + d[l[3].rstrip(")")] + "010" + d[l[1]] + "0000011"
def addi(l,d):
    if int(l[3])==-2**11:
            return decimal_to_twos_complement_12(int(l[3])) + d[l[2]] + "000" + d[l[1]] + "0010011"

    if abs(int(l[3]))>=2**11:
        return "0"
    return decimal_to_twos_complement_12(int(l[3])) + d[l[2]] + "000" + d[l[1]] + "0010011"
def sltiu(l,d):
    if int(l[3])==-2**11:
             return decimal_to_twos_complement_12(int(l[3])) + d[l[2]] + "011" + d[l[1]] + "0010011"

    if abs(int(l[3]))>=2**11:
        return "0"
    return decimal_to_twos_complement_12(int(l[3])) + d[l[2]] + "011" + d[l[1]] + "0010011"
def jalr(l,d, labels, pc):
    

    if l[3] in labels:
        x=decimal_to_twos_complement_12(labels[l[3]]-pc*4)
    else:
        x=decimal_to_twos_complement_12(int(l[3]))
        if int(l[3])==-2**11:
            return x + d[l[2]] + "000" + d[l[1]] + "1100111"
        if abs(int(l[3]))>=2**11:
            return "0"
    return x + d[l[2]] + "000" + d[l[1]] + "1100111"
