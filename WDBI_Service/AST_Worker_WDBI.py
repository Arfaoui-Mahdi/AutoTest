import re
import os
# ### 1 - Function to Read the file containing the AST to explore it 



def readNclearGIME(path):
    tab = []
    tt = []
    j = 0
    with open (path + '-WDBI.txt', 'r') as f:
        txtToExplore = f.read()
    txtToExplore = txtToExplore.split('\n')
    for i in txtToExplore : 
        if i == '' or i == ' ': 
            txtToExplore.remove(i)
    for k in txtToExplore:
        tt = k.split(" : ", 1)
        tab.insert(j,tt)
        j = j + 1
        
    return tab



def extID(tab):

    IDs = []
    count = 0
    for it in range(0,len(tab)) : 
        if len(tab[it]) == 2 and "nodetype" in tab[it][0] :
            if "Case" in tab[it][1] : 
                t = it +1
                while "value" not in tab[t][0] : 
                    t = t + 1
                #print(tab[t][1])
                IDs.insert(count,tab[t][1])
                count = count + 1
    for i in IDs:
        if len(i) != 6 : #cause a RDBI ID is on 2 bytes (exp : 0x0021), thus, length = 6
            IDs.remove(i)
    return IDs