def decimal_to_twos_complement_21(decimal_num):
    if decimal_num < 0:
        abs_decimal = abs(decimal_num)
        complement = 2**21 - abs_decimal
    else:
        complement = decimal_num

    twos = bin(complement)[2:]
    
    if len(twos) < 21:
        twos = '0' * (21 - len(twos)) + twos

    return twos



def jal(l,d, labels, pc):
    if l[2] in labels:
        x=decimal_to_twos_complement_21(labels[l[2]]-pc*4)
    else:
        x=decimal_to_twos_complement_21(int(l[2]))
        if int(l[2])==-2**20:
            return x[0]+x[-11:-1:] + x[-12]+ x[-20:-12:]+ d[l[1]] + "1101111"

        if abs(int(l[2]))>=2**20:
            return "0"
        x=decimal_to_twos_complement_21(int(l[2]))
    return x[0]+x[-11:-1:] + x[-12]+ x[-20:-12:]+ d[l[1]] + "1101111"
