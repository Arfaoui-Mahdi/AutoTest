

from . import AST_Worker_RDBI
import re
from . import ConvertAndExtractParams
#from . import func_defs_ast_extractor
import os
from . import do_it_RDBI

def RDBIS(path, sourcePth, cfgPath):


    # PHASE 1 :
    #do_it_RDBI.buildAstRDBI(path, sourcePth)
        
    astList = AST_Worker_RDBI.readNclearGIME(path)



    idsList = AST_Worker_RDBI.extID(astList)


    # Preparing the cfg.h file to extract IDs names
    headerCode = ConvertAndExtractParams.convCF(cfgPath) # Entering the header file to explore it
    headerCodeList = ConvertAndExtractParams.cleanL(headerCode) # Convert and Clean the header file List to explore it



    rdbiFinal = []
    for i in idsList:
        for j in headerCodeList:
                if i in j and re.findall("\A#define", j):
                    rdbiFinal.append(j)

    

    # Deleting the file after processing
    os.remove(path + "-RDBI.txt")
    return rdbiFinal




