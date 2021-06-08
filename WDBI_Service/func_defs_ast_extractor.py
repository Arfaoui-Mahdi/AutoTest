
from __future__ import print_function
from pycparser import c_parser, c_ast, parse_file
import sys
from . import c_json 
import json
import ast



 



### 1 - Function to Write the AST into a file
def writeFile(tt):
    print("============================" + patsTo + "==================")
    f = open(patsTo + '-WDBI.txt', 'a') 
    f.write(tt)  # writing to a file a simple str
    f.close()    # json.dump(a, f)







### 2 - Function to iterate recursively in the casted AST dict 
# Working on an AST dict, some values might be dict aswell as list or other type structure
# this function take care of these cases and iterate over the whole AST

def iterdict(d):
    for k, v in d.items():
        if isinstance(v, dict):  # if value is a dict ==> iterate again
            
            satt = str(k) + " : "
            writeFile(satt)
            iterdict(v)
     

        elif isinstance(v , list) and len(v) != 0 : #if the value is a list ==> convert to a dict and iterate again
            for i in v : 
                if not isinstance(i, dict):
                    stt = str(i) + "\n\r "
                else :
                    iterdict(i) 
        
        else:                                    # else
            stt =  str(k) + " : " + str(v) + "\n\r "
            writeFile(stt)
           




class FuncDefVisitor(c_ast.NodeVisitor):
    def visit_FuncDef(self, node):
        if node.decl.name == 's32ADoc_iWDBI_Exe':

            JJ = c_json.to_json(node,  separators=(",", ":"), indent=4)
            DD = json.loads(JJ) #convert to dict
            iterdict(DD)

           


def show_func_defs(path, filename):

    ast = parse_file(filename, use_cpp=True,
                     cpp_path='gcc',
                     cpp_args=['-E', r'-Iutils/fake_libc_include', '-D__attribute__(x)=']) #__attribute__ was added 
                                                                                           # to take care of that syntaxe
    global patsTo 
    patsTo = path
    #print("============================" + patsTo + "==================")
    v = FuncDefVisitor()
    v.visit(ast)



