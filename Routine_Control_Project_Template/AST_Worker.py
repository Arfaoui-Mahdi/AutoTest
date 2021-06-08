import re
import os
# ### 1 - Function to Read the file containing the AST to explore it 



def readNclearGIME(path):
    tab = []
    tt = []
    j = 0
    with open(path + "-RC.txt", 'r') as f:
        txtToExplore = f.read()
    txtToExplore = txtToExplore.split('\n')
    for i in txtToExplore : 
        if i == '' or i == ' ': 
            txtToExplore.remove(i)
    for k in txtToExplore:
        tt = k.split(" : ",1)
        tab.insert(j,tt)
        j = j + 1
        
    return tab







# ### 2 - Function to extract Routine IDs
# 


def extRouIDs(tab):

    routineIDs = []
    count = 0
    for it in range(0,len(tab)) : 
        if len(tab[it]) == 2 and "nodetype" in tab[it][0] :
            if "Case" in tab[it][1] : 
                t = it +1
                while "value" not in tab[t][0] : 
                    t = t + 1
                #print(tab[t][1])
                routineIDs.insert(count,tab[t][1])
                count = count + 1
    for i in routineIDs:
        if len(i) != 6 : #cause a sub-routine ID is on 2 bytes (exp : 0x0021), thus, length = 6
            routineIDs.remove(i)
    return routineIDs




# ### 3 - Function to extract Routine IDs Address in the code



def routAdds(routineIDs, tab):
    routineAdds = []
    countAdd = 0
    for j in range (0 , len(routineIDs)):        
        for i in range(0,len(tab)) : 
            if len(tab[i]) == 2 and "value" in tab[i][0] :
                if str(routineIDs[j]) in tab[i][1]:
                    firstElmPos = tab.index(tab[i])
                    routineAdds.insert(countAdd, firstElmPos)
                    countAdd += 1
                    break
    return routineAdds
    

### 4 - Function to extract Routine AST code blocks

def routCodeBlock(routineAdds, tab):
    globalCodeBlocks = []
    countGlob = 0
    first = 0
    secnd = 0
    first = routineAdds[0]
    secnd = routineAdds[1]

    for i in range(1 , len(routineAdds)):
        for j in range (first, secnd-1):
            globalCodeBlocks.insert(countGlob, tab[first:secnd])        
            countGlob = countGlob + 1
            break

        if str(secnd) == str(routineAdds[len(routineAdds)-1]):
            first = secnd
            secnd = len(tab)
            globalCodeBlocks.insert(countGlob, tab[first:secnd])
        else :
            first = routineAdds[i]
            secnd = routineAdds[i+1]
       

    return globalCodeBlocks



