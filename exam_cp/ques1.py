from collections import Counter


def check(d1,d2,n1,n2,count):
    for k1,v1 in d1.items():
        if d1[k1]==d2[k1]:
            count=count+1
    return count



def find(st1,st2):
    s=st1.lower().replace(" ","")
    s2=st2.lower().replace(" ","")
    d1={}
    d2={}
    count=0
    d1=dict(Counter(s))
    d2=dict(Counter(s2))
    n1=len(d1.keys())
    n2=len(d2.keys())


    if n1!=n2:
        return(print(False))
    else:
        c=check(d1,d2,n1,n2,0)
        if c==n1:
           return( print(True))
        else:
            return(print(False))

find("anagram","nagaram")           
find("Keep","Peek")
find("Mother In Law","Hitler Woman")
find("School Master","The Classroom")
find("ASTRONOMERS","NO MORE STARS")
find("Toss","Shot")
find("joy","enjoy")
find("Debit Card","Bad Credit")
find("SiLeNt CAT","LisTen AcT")
find("Dormitory","Dirty Room")

