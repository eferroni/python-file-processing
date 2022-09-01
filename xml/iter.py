import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()

for author in root.iter('author'):
    print(author.text)