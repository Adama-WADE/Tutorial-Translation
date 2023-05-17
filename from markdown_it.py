from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode

with open(r'C:\Users\Adama\Documents\Tutorial-Translation\Marp.md','r', encoding="utf-8") as fin:
    md_ = fin.read()

md = MarkdownIt("commonmark")
tokens = md.parse(md_)

node = SyntaxTreeNode(tokens)
#print(node.pretty(indent=2, show_text=True))
print(node.children[1].children[0].content)

"""
# Header

Here's some text \n and an image ![title](image.png). Some more text here.
This is another sentence.

This is new paragraph. With some more text.

1. a **list**

> a *quote*
"""