import random
import pinyin

noun = open('freqword_n.txt', encoding='utf-8').read().split()
verb = open('freqword_v.txt', encoding='utf-8').read().split()
rhythmList=['a','e','i','o','u','v']
rhythm1=''
rhythm2=''
rhythm4=''

def isping(a):
    pz=pinyin.get(a,format='numerical')[-1]
    if pz=='1' or pz=='2':
        return True
    else:
        return False
def isze(a):
    pz=pinyin.get(a,format='numerical')[-1]
    if pz=='3' or pz=='4':
        return True
    else:
        return False

def writeLine1():
    global nounlist
    global verblist
    global rhythm1
    pz1=''
    pz2=''
    i=random.randint(0,len(noun)-1)
    while isping(noun[i][0]) or isping(noun[i][1]):
        i=random.randint(0,len(noun)-1)
        while isping(noun[i][1]):
            i=random.randint(0,len(noun)-1)
    pz3=''
    pz4=''
    j=random.randint(0,len(verb)-1)
    while isze(verb[j][0]) or isze(verb[j][1]):
        j=random.randint(0,len(verb)-1)
        while isze(verb[j][1]):
            j=random.randint(0,len(verb)-1)
    k=random.randint(0,len(noun)-1)
    while isping(noun[k][1]):
        k=random.randint(0,len(noun)-1)
    verse=pinyin.get(noun[k][1],format='strip')
    ind=0
    for p in range(len(verse)-1,-1,-1):
        if verse[p] in rhythmList:
            ind=p
    rhythm1=verse[ind:]
    return noun[i]+verb[j]+noun[k][1] #名名动动名，仄仄平平仄
def writeLine2():
    global nounlist
    global verblist
    global rhythmList
    global rhythm2
    pz1=''
    pz2=''
    i=random.randint(0,len(noun)-1)
    while isze(noun[i][0]) or isze(noun[i][1]):
        i=random.randint(0,len(noun)-1)
        while isze(noun[i][1]):
            i=random.randint(0,len(noun)-1)
    pz3=''
    pz4=''
    j=random.randint(0,len(verb)-1)
    while isping(verb[j][0]) or isping(verb[j][1]):
        j=random.randint(0,len(verb)-1)
        while isping(verb[j][1]):
            j=random.randint(0,len(verb)-1)
    k=random.randint(0,len(noun)-1)
    while isze(noun[k][1]) or rhythm2!=rhythm1:
        k=random.randint(0,len(noun)-1)
        verse=pinyin.get(noun[k][1],format='strip')
        ind=0
        for p in range(len(verse)-1,-1,-1):
            if verse[p] in rhythmList:
                ind=p
        rhythm2=verse[ind:]
    return noun[i]+verb[j]+noun[k][1] #名名动动名，平平仄仄平
def writeLine3():
    global nounlist
    global verblist
    pz1=''
    pz2=''
    i=random.randint(0,len(noun)-1)
    while isze(noun[i][0]) or isze(noun[i][1]):
        i=random.randint(0,len(noun)-1)
        while isze(noun[i][1]):
            i=random.randint(0,len(noun)-1)
    j=random.randint(0,len(verb)-1)
    while isze(verb[j][1]):
        j=random.randint(0,len(verb)-1)
    k=random.randint(0,len(noun)-1)
    while isping(noun[k][0]) or isping(noun[k][1]):
        k=random.randint(0,len(noun)-1)
        while isping(noun[k][1]):
            k=random.randint(0,len(noun)-1)
    return noun[i]+verb[j][1]+noun[k] #名名动名名，平平平仄仄
def writeLine4():
    global nounlist
    global verblist
    global rhythmList
    global rhythm4
    pz1=''
    pz2=''
    i=random.randint(0,len(noun)-1)
    while isping(noun[i][0]) or isping(noun[i][1]):
        i=random.randint(0,len(noun)-1)
        while isping(noun[i][1]):
            i=random.randint(0,len(noun)-1)
    j=random.randint(0,len(verb)-1)
    while isping(verb[j][1]):
        j=random.randint(0,len(verb)-1)
    k=random.randint(0,len(noun)-1)
    while isze(noun[k][0]) or isze(noun[k][1]) or rhythm4!=rhythm2:
        k=random.randint(0,len(noun)-1)
        verse=pinyin.get(noun[k][1],format='strip')
        ind=0
        for p in range(len(verse)-1,-1,-1):
            if verse[p] in rhythmList:
                ind=p
        rhythm4=verse[ind:]
    return noun[i]+verb[j][1]+noun[k] #名名动名名，仄仄仄平平
f=open('词频写诗结果.txt','w',encoding='utf-8')
for i in range(10):
    print('')
    Line1=writeLine1()
    Line2=writeLine2()
    Line3=writeLine3()
    Line4=writeLine4()
    print(Line1)
    print(Line2)
    print(Line3)
    print(Line4)
    f.write('\n')
    f.write(Line1+'\n')
    f.write(Line2+'\n')
    f.write(Line3+'\n')
    f.write(Line4+'\n')
f.close()
