

import os, sys
from . import AST_Worker_WDBI
import re
from . import ConvertAndExtractParams
#from . import func_defs_ast_extractor
from . import do_it_WDBI

def WDBIS(path, sourcePth, cfgPath):



    # PHASE 1 :
    #do_it_WDBI.buildAstWDBI(path, sourcePth)

    astList = AST_Worker_WDBI.readNclearGIME(path)



    idsList = AST_Worker_WDBI.extID(astList)



    # Preparing the cfg.h file to extract IDs names
    headerCode = ConvertAndExtractParams.convCF(cfgPath) # Entering the header file to explore it
    headerCodeList = ConvertAndExtractParams.cleanL(headerCode) # Convert and Clean the header file List to explore it


    wdbiFinal = []
    for i in idsList:
        for j in headerCodeList:
                if i in j and re.findall("\A#define", j): #Extract only header that begins with #define
                    wdbiFinal.append(j)

    
    # Deleting the file after processing
    os.remove(path + "-WDBI.txt")

    return wdbiFinal












