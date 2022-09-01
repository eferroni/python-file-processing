import xml.etree.ElementTree as ET


def add_sub_element(parent, name, attributes, text=None):
    sub_element = ET.SubElement(parent, name, attributes)
    sub_element.text = text
    return sub_element


shop = ET.Element('shop')

category = add_sub_element(shop, 'category', {'name': 'Vegan Products'})
prod_1 = add_sub_element(category, 'product', {'name': 'Good Morning Sunshine'})
add_sub_element(prod_1, 'type', {}, 'cereals')
add_sub_element(prod_1, 'producer', {}, 'OpenEDG Testing Service')
add_sub_element(prod_1, 'price', {}, '9.90')
add_sub_element(prod_1, 'currency', {}, 'USD')

prod_2 = add_sub_element(category, 'product', {'name': 'Spaghetti Veganietto'})
add_sub_element(prod_2, 'type', {}, 'pasta')
add_sub_element(prod_2, 'producer', {}, 'Programmers Eat Pasta')
add_sub_element(prod_2, 'price', {}, '15.49')
add_sub_element(prod_2, 'currency', {}, 'EUR')

prod_3 = add_sub_element(category, 'product', {'name': 'Fantastic Almond Milk'})
add_sub_element(prod_3, 'type', {}, 'beverages')
add_sub_element(prod_3, 'producer', {}, 'Drinks4Coders Inc.')
add_sub_element(prod_3, 'price', {}, '19.75')
add_sub_element(prod_3, 'currency', {}, 'USD')

ET.dump(shop)

tree = ET.ElementTree(shop)
tree.write('shop.xml', 'UTF-8', True)