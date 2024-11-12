def rst():
    return "0000001"+"0"*25
def halt():
    return "0000010"+"0"*25
def rvrs(l,d):
    return "0000100"+"0"*5+d[l[2]]+"0"*3+d[l[1]]+"0"*7
