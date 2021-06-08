import AST_Worker
import ConvertAndExtractParams
import func_defs_ast_extractor
import re


# PHASE 1 :
filename = r'C:/Users/Mahdi/Desktop/WORK_Field/TEEEEEEEEEEST/doc_app.c' # Choose the main source file to explore
func_defs_ast_extractor.show_func_defs(filename) # Extract the AST for a specified Service and write to a file to explore it

# PAHSE 2 :
txtTab = AST_Worker.readNclearGIME() # Building the AST into a List form
routineIDs = AST_Worker.extRouIDs(txtTab) # Extracting routine IDs
routineAdds = AST_Worker.routAdds(routineIDs,txtTab) # Extracting each routine Add
globalCodeBlocks = AST_Worker.routCodeBlock(routineAdds, txtTab) # Extracting each routine AST code Block


#PHASE 3 :
txtCode = ConvertAndExtractParams.convCF('doc_app.c') # Converting source code into text to explore it
codeList = ConvertAndExtractParams.cleanL(txtCode) # Clean the text and form it into list
paramsNum = ConvertAndExtractParams.coordInp(globalCodeBlocks, txtCode) # Number of params for each sub-routin


headerCode = ConvertAndExtractParams.convCF('doc_app_cfg.h') # Entering the header file to explore it
headerCodeList = ConvertAndExtractParams.cleanL(headerCode) # Convert and Cleand the header file List to explore it

final = []
count = 0

for i in range(0,len(routineIDs)):
    for j in headerCodeList:
        if routineIDs[i] in j:
            final.insert(count, [j, paramsNum[i]])    
            count += 1


for i in final:
    print(i)
