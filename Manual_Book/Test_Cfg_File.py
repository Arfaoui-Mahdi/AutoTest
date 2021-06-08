import re
import sys

def convCF(paath):
    txt=[]
    count = 0
    crimefile = open(paath, 'r') 
    for line in crimefile: 
        txt.insert(count,line)
        count = count +1
    crimefile.close()
    return txt

 


# ### 2 - Cleaning list

def cleanL(txt):
    for i in range(0,len(txt)):
        txt[i] = txt[i].replace("\n","")
        txt[i] = txt[i].strip()
        #if i == "" or i == " ":
           # txt.remove[txt[i]]
    return txt


def DO(filename):
    res1 = convCF(filename)
    res2 = cleanL(res1)
    for i in res2:
        print(str(i))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename  = sys.argv[1]
        DO(filename)