import xmltodict

def processXML(filename):
    with open(filename) as XMLFile:
        return xmltodict.parse(XMLFile.read())

products = processXML('products.xml')
products = products['artikelen']['artikel']

for product in products:
    print(product['naam'])
