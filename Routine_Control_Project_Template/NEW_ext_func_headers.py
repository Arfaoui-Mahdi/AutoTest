
from pycparser import c_parser, c_ast, parse_file
import re 
import json
import sys
from io import StringIO




def ext_func_coords(filename):

    res = []
    
    ast = parse_file(filename, use_cpp=True,
            cpp_path='gcc',
            cpp_args=['-E', r'-Iutils/fake_libc_include', '-D__attribute__(x)='])
    #ast.show()
    for i in ast.ext:
        holder = []    
        if "pycparser.c_ast.Decl" in str(type(i))  : # Check if the node is a declaration or not
            if i.name  :
               
                k = re.findall(":[0-9]*:", str(i.coord))
                l = k[0][1:len(k)-2]
                #if  i.type.args != None :
                if hasattr(i.type, 'args'): # Verifying if a decl obj has args or not, if YES, extract params list
                   # print("NAAAAME : %s" % (i.name))
                    if hasattr(i.type.args, 'params'):
                        for param_decl in i.type.args.params:
                            var = StringIO()
                            
                            #print('Arg name: %s' % param_decl.name)
                            #print('Type:')
                            param_decl.type.show(buf= var, offset=6)
                            #JJ = to_json(param_decl.type,  separators=(",", ":"), indent=4)
                            #DD = json.loads(JJ) 
                            #if "declname" in DD.keys() :
                                #print("variable name : %s, it's type is %s : " %( str(DD["declname"]), str(DD["type"]["names"])))
                            #print(DD)
                            #print("this is holder")
                            
                            
                            #print(type(var.getvalue()))
                            #print("\n")
                            tmp1 = 'Arg Name : ' + str(param_decl.name)
                            tmp2 = 'Arg Type : ' + var.getvalue()
                            holder.append([tmp1, tmp2])
                        res.append([i.name, holder])
                    #else :                          # Declarations without args are not function decls
                                                    # cause even when a function have no args (it has void)
                                                    # the parser indicates a void argument in its output
                                                    # that's why it is ignored
                    #   print("bbbbbb %s" %(i.name))
                    #  res.append([i.name, None])

    return res
        

 