
from WDBI_Service import WDBI_Project
from Routine_Control_Project_Template import Routine_Control_Project
from RDBI_Service import RDBI_Project
import func_defs_ast_extractor
import sys
import re
import json



def extArgsLists(ff):
    temp = []
    table = []
    
    temp = []
    
    for j in ff: #each service
        if isinstance(j,list):
            if j[1] is not None :
                if isinstance(j[1], list): #each list of args
                    for t in j[1]: #each arg
                        #print(t[0]) #it holds the names
                        m = t[0]
                        m = m.split(":")
                        temp.append(m[1].strip())
    table.append(temp)
    return table


def doWork(path, srcPath, cfgPath, incPath):

    func_defs_ast_extractor.show_func_defs(path, srcPath)

    wdbi = WDBI_Project.WDBIS(path, srcPath, cfgPath)
    rdbi = RDBI_Project.RDBIS(path, srcPath, cfgPath)
    rc = Routine_Control_Project.RCS(path, srcPath, cfgPath, incPath)


    with open (path + ".txt" , 'x' ) as f: 
        f.write("\n=====================================\n Routine Control \n=====================================\n\n")
        for i in rc : 
            f.write(str(i))
            f.write("\n\n")
        f.write("\n=====================================\n WDBI \n=====================================\n\n")
        for i in wdbi : 
            f.write(str(i))
            f.write("\n")
        f.write("\n=====================================\n RDBI \n=====================================\n\n")
        for i in rdbi : 
            f.write(str(i))
            f.write("\n")

    count = 0

    listRC = []
    
    for i in rc : 
        argList = extArgsLists(i[1]) # Routine that have argument = None, mean that they call functinos withou params
        count = 0
        for j in i[1]:
            #count = count + len(j[1])
            if isinstance(j, list):
                count = count + len(j[1])
        i[0] = i[0].strip()
        i[0] = i[0].replace("#define", "")
        i[0] = i[0].strip()
        t = re.findall("0x[a-zA-Z0-9]{4}", i[0])
        #print(i[0])
    
        i[0]=i[0].split(" ")
        k = i[0][0]
        if k.split(" ") :
            r = k.split()[0]
        #print(k , t[0])
        # print("\n")
        temp = [r , t[0] , count, argList[0]]
        listRC.append(temp)
    
    # Serializing json 
    json_object = json.dumps(listRC, indent = 4)
    
    # Writing to sample.json
    with open(path + "-RC" +".json", "x") as outfile:
        outfile.write(json_object)


    # Handling WDBI Service
    listWDBI = []
    for i in wdbi : 
        i = i.strip()
        i = i.replace("#define", "")
        i = i.strip()
        idd = re.findall("0x[a-zA-Z0-9]{4}", i)
        idd = idd[0]
        i = i.split(" ")
        print(i)
        name = i[0]
        listWDBI.append([name,idd])
    jsonWDBI = json.dumps(listWDBI, indent = 4)
    with open(path + "-WDBI" +".json", "x") as wdbiF:
        wdbiF.write(jsonWDBI)

    # Handling RDBI Service
    listRDBI = []
    for i in rdbi : 
        i = i.strip()
        i = i.replace("#define", "")
        i = i.strip()
        idd = re.findall("0x[a-zA-Z0-9]{4}", i)
        idd = idd[0]
        i = i.split(" ")
        name = i[0]
        listRDBI.append([name,idd])
    jsonRDBI = json.dumps(listRDBI, indent = 4)
    with open(path + "-RDBI" +".json", "x") as rdbiF:
        rdbiF.write(jsonRDBI)






if __name__ == "__main__":
    args = sys.argv
    path = args[1] # Cause the first arg is the path of this file
    srcPath = args[2]
    cfgPath = args[3]
    incPath = args[4]
    doWork(path, srcPath, cfgPath, incPath)










