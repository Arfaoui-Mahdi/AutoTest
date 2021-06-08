from . import func_defs_ast_extractor
import re


# PHASE 1 :
def buildAstRDBI(path, filename):
    func_defs_ast_extractor.show_func_defs(path, filename) # Extract the AST for a specified Service and write to a file to explore it
