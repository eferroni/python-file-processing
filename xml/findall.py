import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()

for author in root.findall('author'):
    print(author.text)

for book in root.findall('book'):
    print(book.get('title'))