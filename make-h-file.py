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

#variable to count the number of horizontal rules
hr_count = 0
between_hr = True

def extract_text(node):
    global hr_count, between_hr
    if node.type == "hr":
        hr_count += 1
        if hr_count == 2:
            between_hr = False

    if between_hr:
        if node.type == "inline" and not any(child.type == "image" for child in node.children):
            fout.write('\n')  # Write an empty line for inline elements between the first and second "hr" elements
    else:
        if node.type == "inline" and not any(child.type == "image" for child in node.children):
            fout.write(node.content + '\n')

    for child in node.children:
        if isinstance(child, SyntaxTreeNode) and child.type != "image":
            extract_text(child)

    
with open('output1.txt', 'w', encoding="utf-8") as fout:       
    extract_text(treeRoot)
# Write to test.h
with open('output1.txt', 'r', encoding="utf-8") as fin, open('test.h', 'w', encoding="utf-8") as fout:
    for line in fin:
        curr_line = line.strip()
        fout.write('QT_TRANSLATE_NOOP("Data Visualization Tutorial", "' + curr_line + '")\n')