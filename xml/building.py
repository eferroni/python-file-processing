import xml.etree.ElementTree as ET

root = ET.Element('data')

movie_1 = ET.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})
movie_2 = ET.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '4'})

ET.dump(root)

tree = ET.ElementTree(root)
tree.write('movie_builded.xml', 'UTF-8', True)