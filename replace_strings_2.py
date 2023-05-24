from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode
import xml.etree.ElementTree as ET

# XML parsing
tree = ET.parse('test1.ts')
ts_root = tree.getroot()
print(ts_root[0][1][0].tag, ts_root[0][1][0].attrib)


#Markdown parsing
with open('Marp_french.md', 'r', encoding="utf-8") as f: 
            md = f.read()
            parser = MarkdownIt("commonmark")
            tokens = parser.parse(md,)
            md_root = SyntaxTreeNode(tokens)


def translate_tree(node, translation_tree):
    print(node.type)
    if node.type == "text":
        # print(node.content)
        for translation_node in ts_root[0].findall('message'):
            source = translation_node.find('source').text
            # print(source)
            translation = translation_node.find('translation').text
            print(translation)
            if source == node.content:
                node.content = translation
                break

    for child_node in node.children:
        if isinstance(child_node, SyntaxTreeNode):
            translate_tree(child_node, translation_tree)

translate_tree(md_root, ts_root) 
