
from __future__ import print_function
import sys

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
sys.path.extend(['.', '..'])

from pycparser import c_parser, c_ast, parse_file


# A simple visitor for FuncDef nodes that prints the names and
# locations of function definitions.
class FuncDefVisitor(c_ast.NodeVisitor):
    def visit_FuncDef(self, node):
        print('%s at %s' % (node.decl.name, node.decl.coord))


def show_func_defs(filename):
   
    ast = parse_file(filename, use_cpp=True,
                     cpp_args=[r'-Iutils/fake_libc_include', '-D__attribute__(x)='])

    v = FuncDefVisitor()
    v.visit(ast)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename  = sys.argv[1]
    

    show_func_defs(filename)