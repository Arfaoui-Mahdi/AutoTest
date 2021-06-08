



import re


# ### 1 - Converting the C file into a list of lines



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



# FROM HERE >> NOT USED

# ### 3 - Function to extract coord where "Prepare Input" is placed

def coordInp(glob, txtCode):
    coordStrt = []
    count = 0
    for i in glob:
        x = re.findall("[0-9]{4}",i[1][1])
        x = int(x[0])
        coordStrt.insert(count, x)
        count += 1
    lastCase = glob[len(glob)-1] # last routine code block
    last = len(lastCase)-1 # index of last line in the last routine code block
    flag = True
    curr = last
    
    while(flag):
        if "coord" in lastCase[curr][0]: #when it find the first element containing "coord"
            x = re.findall("[0-9]{4}",lastCase[curr][1]) # it extracts it's coord line in the code
            x = int(x[0])
            coordStrt.insert(count, x)
            flag = False
        curr -= 1
    cc = 0
    finalParms = []
    k = 0
    
    for i in range (0, len(glob)):
        first = coordStrt[k]
        secnd = coordStrt[k+1]
        for j in range(first, secnd):
            if "Prepare Input" in txtCode[j] or "input" in txtCode[j]:
                finalParms.insert(cc, extParams(j, txtCode))
                cc += 1
                break 
            elif j == (secnd-1):
                finalParms.insert(cc, 0)
                cc += 1
        k = k + 1
                 
    
    return finalParms
    
    



def extParams(beg, txt):
    count = 0
    x = beg + 1
    verF = "TmpVar"
    while("Call API Service" not in txt[x]):
        if verF in txt[x]:
            count += 1
        x += 1 
    return count

