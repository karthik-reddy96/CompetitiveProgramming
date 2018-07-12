
global d
d={
"A" :".-",
"B":"-...",
"C" :"-.-.",
"D" :"-..",
"E" :".",
"F":"..-.",
"G" :"--.",
"H" :"....",
"I":"..",
"J":".---",
"K":"-.-",
"L":".-..",
"M":"--",	
"N":"-.",
"O":"---",
"P":".--.",
"Q":"--.-",
"R":".-.",
"S":"...",
"T":"-",
"U":"..-",
"V":"...-",
"W":".--",
"X":"-..-",
"Y":"-.--",
"Z":"--.."
}

def morse(st):
    global d
    stri=st.upper()
    lis=list(stri)
    
    s=""
    for i in lis:

        s=s+d[i]
    return s

y=morse("gin")

def inp(lis):
    list1=[]
    for i in lis:
        y=morse(i)
        list1.append(y)
    s=set(list1)
    count=len(s)
    return count
        
        

print(inp(["gin", "zen", "gig", "msg"]))
print(inp(["a", "z", "g", "m"]))

print(inp(["bhi", "vsv", "sgh", "vbi"]  ))
print(inp(["a","b","c","d"]))
print(inp(["hig", "sip", "pot"]  ))
