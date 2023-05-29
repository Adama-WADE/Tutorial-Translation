from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode
import xml.etree.ElementTree as ET

# XML parsing
tree = ET.parse('test1.ts')
ts_root = tree.getroot()
print(ts_root[0][1][0].tag, ts_root[0][1][0].attrib)


#Markdown parsing
""" with open('Marp_french.md', 'r', encoding="utf-8") as f: 
            md = f.read()
            parser = MarkdownIt("commonmark")
            tokens = parser.parse(md,)
            md_root = SyntaxTreeNode(tokens) """

def replace_strings_in_markdown(markdown_file, translation_tree):
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    for message_node in translation_tree[0].findall('message'):
        source = message_node.find('source').text
        print(source)
        translation = message_node.find('translation').text
        print(translation)
        markdown_text = markdown_text.replace(source, translation)

    with open(markdown_file, 'w', encoding='utf-8') as f:
        f.write(markdown_text)

replace_strings_in_markdown('Marp_french.md', ts_root)
