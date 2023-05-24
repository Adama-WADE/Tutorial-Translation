'''
This is in the progress of converting from json to syntax tree
'''
# Import statements
# import commonmark
# import json
from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode

# Read in Marp.md file
with open(r'C:\Users\Adama\Documents\Tutorial-Translation\Marp.md','r', encoding="utf-8") as fin:
    md_ = fin.read()

# Parse the markdown file 
# parser = commonmark.Parser()
# ast = parser.parse(md)
md = MarkdownIt("commonmark")
tokens = md.parse(md_)

# Json representation is simple but does not include source location
# jsonRoot = json.loads(commonmark.dumpJSON(ast))
treeRoot = SyntaxTreeNode(tokens)

# with open('output.txt', 'w', encoding="utf-8") as fout:
#     for item in jsonRoot:
#         if item['children']:
#             for childItem in item['children']:
#                 if "literal" in childItem:
#                     fout.write(childItem["literal"] + '\n')

# # Write to test.h
# with open('output.txt', 'r', encoding="utf-8") as fin, open('test.h', 'w', encoding="utf-8") as fout:
#     for line in fin:
#         curr_line = line.strip()
#         fout.write('QT_TRANSLATE_NOOP::tr("' + curr_line + '")\n')

# Write literal content to output.txt
# Write literal content to output.txt
with open('output.txt', 'w', encoding="utf-8") as fout:
    def extract_text(node):
        print(node.type)
        if node.type == "text":
            fout.write(node.content + '\n')
        for child in node.children:
            if isinstance(child, SyntaxTreeNode) and child.type != "image":
                extract_text(child)
    extract_text(treeRoot)
# Write to test.h
with open('output.txt', 'r', encoding="utf-8") as fin, open('test.h', 'w', encoding="utf-8") as fout:
    for line in fin:
        curr_line = line.strip()
        fout.write('QT_TRANSLATE_NOOP("Data Visualization Tutorial", "' + curr_line + '")\n')