


from . import NEW_ext_func_headers
import re
from . import ConvertAndExtractParams
from . import AST_Worker
#from . import func_defs_ast_extractor
import os
from . import do_it_RC






def retSerFunArgs(names, funcDefsArgs): # Function to return service specification from "funcDefsArgs" giving the service name(s)
    res = []
    if names:
        for i in names:
            for j in funcDefsArgs:
                if str(i) == str(j[0]):
                    res.append(j)
                    break
    else :
        return [None] # The routine have a function call without any args
                
    return res
        



def extServNames(A) : 
    names = []
    for i in range(0 , len(A)): # For eeach line in a sub routine AST
        if (len(A[i]) == 2) and ("FuncCall" in A[i][1] ):
            x = A[i+3][1] # the name of the service exist in the third element after this element -- to explore more -- (SO FAR SO GOOOD !!)
            names.append(x) # Extract service names of the sub routine
    return names
    





def RCS(path, sourcePth, cfgPath, incPath):
    # ### Preparing the AST Tree for the Routine Control service
    # PHASE 1 :
    #do_it_RC.buildAst(path, sourcePth)
    


    txtTab = AST_Worker.readNclearGIME(path) # Building the AST into a List form
    routineIDs = AST_Worker.extRouIDs(txtTab) # Extracting routine IDs
    routineAdds = AST_Worker.routAdds(routineIDs,txtTab) # Extracting each routine Add
    globalCodeBlocks = AST_Worker.routCodeBlock(routineAdds, txtTab) # Extracting each routine AST code Block






    # ### Extracting Servieces names + codes + params form header files




    # This process will extract the AST of each header file, explore each AST to extract each function call with it's args
    # and then for a List containing the path where these functions(services) are defined and name of each service with args



    


    funcDefsArgs = []  # This list will hold services indices in this form : [ [service_name1, args + type][service_name2, args + type]...]
            
            
    # This two structers were made to track the exchange of data, cause we dispose of multiple header files
    # containing different and similar services, and to organize the results we should track each header seperatly
        
    directory = incPath
    for filename in os.listdir(directory): # Iterating the whole "Include" folder
        if re.findall("\Absp", filename) or re.findall("\ALib", filename) : #************ find solution to parse all header FILES**********                                                        
            paath = os.path.join(directory, filename)
            t = NEW_ext_func_headers.ext_func_coords(paath)
            for m in t:
                funcDefsArgs.append(m)
            




    # Preparing the cfg.h file to extrct routine names
    headerCode = ConvertAndExtractParams.convCF(cfgPath) # Entering the header file to explore it
    headerCodeList = ConvertAndExtractParams.cleanL(headerCode) # Convert and Clean the header file List to explore it



    Finalll = []
   
    for A in globalCodeBlocks: # Assuming that only sub-routines makes function calls, that's how we gonna eliminate 
                            # the non sub-routin caught with their values in the AST (to verify) == VERIFIED !! GOOD TO GOOOO
    
        names = extServNames(A)     
        params = retSerFunArgs(names, funcDefsArgs) 
        #print(A[0][1])
        for j in headerCodeList:
            if A[0][1] in j and re.findall("\A#define", j): # Extract sub routine name from the ID value
                Finalll.append([j, params])  
        
    
    # Deleting the file after processing
    os.remove(path + "-RC.txt")
    return Finalll        
                        

        


    


