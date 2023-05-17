# with open(r'C:\Users\Adama\Documents\Tutorial-Translation\test.ts','r', encoding="utf-8") as fin:
#     ts = fin.read()
import commonmark
import json
import xml.etree.ElementTree as ET

tree = ET.parse('test.ts')
root = tree.getroot()
print(root[0].tag, root[0].attrib)


for x in root[0].findall('message'):
    source =x.find('source').text
    translation = x.find('translation').text
    with open(r'Marp_french.md','r+', encoding="utf-8") as f:
        md = f.read()
        parser = commonmark.Parser()
        ast = parser.parse(md)
        jsonRoot = json.loads(commonmark.dumpAST(ast))
        for item in jsonRoot:
            if item['children']:
                for childItem in item['children']:
                    if "literal" in childItem:
                        if source == childItem["literal"]:
                            position = childItem["sourcepos"]
                            f.seek(position[0][0])
                            f.write(translation)
                            print(source)
                            print(childItem["literal"])
                            break
