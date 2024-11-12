def binary_to_decimal(binary):
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


def auipc(s,d,pc):
    d[s[-12:-7:]]= db(pc + binary_to_decimal(s[-32:-12:]+'0'*12))
    return d

def lui(s,d):
    d[s[-12:-7:]]= (s[-32:-12:]+'0'*12)
    return d
def check(s,d,pc):
    if s[-7::]=="0110111":
        return lui(s,d)
    elif s[-7::]=="0010111":
        return auipc(s,d,pc)
    else:
        return d
