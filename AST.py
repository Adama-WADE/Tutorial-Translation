import commonmark
                                                                            import json
                                                                            
with open(r'C:\Users\Adama\Documents\Tutorial-Translation\Marp.md','r', encoding="utf-8") as fin:
    md = fin.read()

parser = commonmark.Parser()
ast = parser.parse(md)

# Json representation is simple but does not include source location
""" jsonRoot = json.loads(commonmark.dumpJSON(ast))
for item in jsonRoot:
    if item['children']:
        for childItem in item['children']:
            if "literal" in childItem:
                print(childItem["literal"]) """

# AST object API is more complicated but necessary, as it includes row/column information for each block
commonmark.dumpAST(ast) # pretty print generated AST structure

paragraphs = ''
for node in ast.walker():
    if node[0].t == "paragraph":
        paragraphs += " "
        if node[0].first_child.literal:
            paragraphs += node[0].first_child.literal + "\n"
