from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode
import xml.etree.ElementTree as ET

# XML parsing
tree = ET.parse('test1.ts')
root = tree.getroot()
print(root[0].tag, root[0].attrib)

""" with open('Marp_french.md', 'r', encoding="utf-8") as f:
    md = f.read()
    parser = MarkdownIt("commonmark")
    nodes = parser.parse(md)
    ast = SyntaxTreeNode(nodes)
    for x in root[0].findall('message'):
        source = x.find('source').text
        # print(source)
        translation = x.find('translation').text
        # print(translation)
        replace_count = 0
        for node in ast.walk():
            if isinstance(node, SyntaxTreeNode) and node.type == 'text' and node.content == source:
                node.content = translation
                print(node.content)
                replace_count += 1

        print(f'Replaced {replace_count} occurrence(s) of "{source}" with "{translation}"')"""

#re-writing the recursive function from make-h-file.py to perform replacement in the markdown file

        # with open('output.txt', 'w', encoding="utf-8") as fout:
#parsing the markdown file
with open('Marp_french.md', 'r', encoding="utf-8") as f: 
            md = f.read()
            parser = MarkdownIt("commonmark")
            nodes = parser.parse(md)
            ast = SyntaxTreeNode(nodes)

def replace_text(node):
    # traverse the list of messages in the parsed ts file and get the source and translation for each message
    for x in root[0].findall('message'):
        source = x.find('source').text
        translation = x.find('translation').text
        def find_match(node):
            if node.type == "text" and node.content == source:
                node.content = translation
                print(node.content)
                for child in node.children:
                    # if isinstance(child, SyntaxTreeNode) and child.type != "image":
                    if isinstance(node, SyntaxTreeNode):
                        replace_text(child)
    if node.type == "text" and node.content == source:
        node.content = translation
        print(node.content)
        for child in node.children:
            # if isinstance(child, SyntaxTreeNode) and child.type != "image":
            if isinstance(node, SyntaxTreeNode):
                replace_text(child)
# Save the modified Markdown back to the file
# with open('Marp_french1.md', 'w', encoding="utf-8") as f:
#     f.write(parser.render(ast))