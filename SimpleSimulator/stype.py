def bd(binary):
    if binary[0] == '1':
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary)
        inverted_decimal = int(inverted_binary, 2) + 1
        decimal = -inverted_decimal
    else:
        decimal = int(binary, 2)

    return decimal

def decimal_to_hexadecimal(decimal_num):
    hexadecimal_num = str(hex(decimal_num))
    hexadecimal_num='0x'+'000'+hexadecimal_num[2:]
    return hexadecimal_num

def sw(s,d,datamem):
    imm=s[-32:-25]+s[-12:-7]
    mem=decimal_to_hexadecimal(bd(d[s[-20:-15]])+(bd(imm)))
    datamem[mem]=d[s[-25:-20]]
    return datamem

def check(s, d,datamem):
    if s[17:20]=="010":
        datamem=sw(s, d,datamem)
        return datamem
