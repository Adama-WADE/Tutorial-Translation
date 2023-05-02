import commonmark
import json

with open(r'C:\Users\Adama\Documents\Tutorial-Translation\Marp.md','r', encoding="utf-8") as fin:
    md = fin.read()

parser = commonmark.Parser()
ast = parser.parse(md)

# Json representation is simple but does not include source location
jsonRoot = json.loads(commonmark.dumpJSON(ast))
with open('output.txt', 'w', encoding="utf-8") as fout:
    for item in jsonRoot:
        if item['children']:
            for childItem in item['children']:
                if "literal" in childItem:
                    fout.write(childItem["literal"] + '\n')
