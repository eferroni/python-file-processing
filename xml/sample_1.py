import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
print('The root element is: ', root.tag)
print('childrens:')
for child in root:
    print('\t', child.tag, child.attrib)