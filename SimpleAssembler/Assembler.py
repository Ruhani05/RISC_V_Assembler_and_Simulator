import btype as b
import itype as i
import jtype as j
import rtype as r
import stype as s
import utype as u
import sys
def split(string):
    global fin
    global fout
    global pc
    global output_
    temp="";
    l=[];
    for i in string:
        if i == " " or i == "," or i=='(':
            l.append(temp);
            temp="";
            continue;
        else:
            temp+=i;
    if temp=="":
        fout.close()
        fout=open(output_,"w")
        fout.write("TYPO ERROR AT LINE "+str(pc+1))
        fin.close()
        fout.close()
        exit()
    if temp[-1]==')':
        temp=temp[:-1]
    l.append(temp);
    return l;

d={"zero" : "00000", "ra":"00001", "sp": "00010", "gp":"00011", "tp":"00100", "t0":"00101", "t1":"00110", "t2":"00111", "s0":"01000", "fp":"01000", "s1":"01001", "a0":"01010", "a1":"01011", "a2": "01100", "a3":"01101", "a4":"01110", "a5":"01111", "a6":"10000", "a7":"10001", "s2":"10010", "s3":"10011", "s4": "10100", "s5":"10101", "s6":"10110", "s7":"10111", "s8":"11000", "s9":"11001", "s10": "11010", "s11":"11011", "t3": "11100", "t4":"11101", "t5":"11110", "t6":"11111"};
rtype=["add", "sub", "sll", "slt", "sltu", "xor", "srl", "or", "and"]
btype=["beq", "bne", "blt", "bge", "bltu", "bgu","bgeu"] 
itype=["lw","addi","sltiu","jalr"]
jtype=["jal"]
utype=["auipc","lui"]
stype=["sw"]
labels={};
pc=0
input_=sys.argv[1]
output_=sys.argv[2]
fin=open(input_, "r")
fout = open(output_, "w")
for line in fin:
    if line=="\n":
        continue;
    l=split(line.lstrip(" "));
    if len(l)>4:
        if(l[0][-1]==":"):
            labels[l[0][:-1]]=pc*4;
        else:
            fout.write("TYPO ERROR AT LINE " + str(pc+1))
            exit()
    if l[1] in ["lui", "auipc"] and len(l)!=3:
        labels[l[0][:-1]]=pc*4;
    if l[1]=="jal":
        labels[l[0][:-1]]=pc*4;
    if l[0] in ["lui","auipc"] and len(l)!=3:
        fout.close()
        fout=open(output_,"w")
        fout.write("SYNTAX ERROR AT LINE "+str(pc+1))
        fin.close()
        fout.close()
        exit()
    pc+=1

pc=0
halt = 0
fin.seek(0)

for line in fin:
    if line=="\n":
        continue;
    if pc!=0:
        fout.write("\n")
    l=split(line.lstrip(" ").rstrip("\n"));
    if len(l)>4:
        l=l[1::];
    if l[1] in ["lui", "auipc"] and len(l)!=3:
        l=l[1::]
    if l[1]=="jal":
        l=l[1::]
    if l == ["beq", "zero", "zero", "0"]:
        halt=pc
    d1={}
    str1=""
    try:
        if l[0] in rtype:
            d1={"add":r.add(l, d), "sub":r.sub(l, d),"sll":r.sll(l, d),"slt":r.slt(l, d),"sltu":r.sltu(l, d),"xor":r.xor(l, d),"srl":r.srl(l, d),"or":r.ory(l, d),"and":r.andy(l, d)};
            str1=d1[l[0]]
        elif l[0] in btype:
            d1={"beq":b.beq(l, d, labels, pc), "bne":b.bne(l, d, labels, pc), "blt":b.blt(l, d, labels, pc), "bge":b.bge(l, d, labels, pc), "bltu":b.bltu(l, d, labels, pc), "bgeu":b.bgeu(l, d, labels, pc)}
            str1=d1[l[0]]
        elif l[0] in itype:
            if l[0]=="lw":
                str1=i.lw(l, d)
            else:
                d1={"addi":i.addi(l,d),"sltiu":i.sltiu(l,d),"jalr":i.jalr(l,d,labels,pc)}
                str1=d1[l[0]]
        elif l[0] in stype:
            d1={"sw":s.sw(l,d)}
            str1=d1[l[0]]
        elif l[0] in jtype:
            d1={"jal":j.jal(l, d, labels, pc)}
            str1=d1[l[0]]
        elif l[0] in utype:
            d1={"auipc":u.auipc(l,d),"lui":u.lui(l,d)}
            str1=d1[l[0]]
        else:
            fout.close()
            fout=open(output_, "w")
            temp="INSTRUCTION AT LINE " + str(pc+1) + " NOT IN ISA"
            fout.write(temp)
            fout.close()
            fin.close()
            exit()
        if str1=="0":
            fout.close()
            fout=open(output_, "w")
            temp="MEMORY OVERFLOWN AT LINE " + str(pc+1)
            fout.write(temp)
            fout.close()
            fin.close()
            exit()
    except :
        if str1=="0":
            exit()
        fout.close()
        fout=open(output_, "w")
        temp="SYNTAX ERROR AT " + str(pc+1)
        fout.write(temp)
        fout.close()
        fin.close()
        exit()
    fout.write(str1)
    pc+=1
halt+=1
if(halt!=pc):
    fout.close()
    fout=open(output_, "w")
    fout.write("SYSTEM EXIT NOT AT END")
    fout.close()
    fin.close()
    exit()

fin.close()
fout.close()
