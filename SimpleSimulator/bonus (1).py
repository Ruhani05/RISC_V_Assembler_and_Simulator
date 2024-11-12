def rst(d):
    d=dict.fromkeys(d.keys(),"0"*32)
    d['00010']="00000000000000000000000100000000"
    return d
def rvrs(rs,rd,d):
    d[rd]=d[rs][::-1]
    return d
def check(s,d,pc):
    if s[0:7]=='0000001':
        d=rst(d)
    elif s[0:7]=='0000100':
        d=rvrs(s[12:17],s[20:25],d)
    return d
