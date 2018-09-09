import csv

product_info = [
    { 'articlenum': 121, 'articlecode': 'ABC123', 'name': 'Highlight pen', 'stock': 231, 'price': 0.56 },
    { 'articlenum': 123, 'articlecode': 'PQR678', 'name': 'Nietmachine', 'stock': 587, 'price': 9.99 },
    { 'articlenum': 128, 'articlecode': 'ZYX163', 'name': 'Bureaulamp', 'stock': 34, 'price': 19.95 },
    { 'articlenum': 137, 'articlecode': 'MLK709', 'name': 'Monitorstandaard', 'stock': 66, 'price': 32.50 },
    { 'articlenum': 271, 'articlecode': 'TRS665', 'name': 'Ipad hoes', 'stock': 155, 'price': 19.01 }
]

with open('products.csv', 'w', newline='\n') as WriteCSVFile:
    writer = csv.writer(WriteCSVFile, delimiter=';')
    writer.writerow(('articlenum', 'articlecode', 'name', 'stock', 'price'))

    for product in product_info:
        writer.writerow((
            product['articlenum'],
            product['articlecode'],
            product['name'],
            product['stock'],
            product['price']
        ))

with open('products.csv', 'r', newline='\n') as ReadCSVFile:
    top = { 'name': '', 'price': 0.0 }
    low = { 'articlenum': 0, 'stock': 1000 }
    total_stock = 0
    reader = csv.DictReader(ReadCSVFile, delimiter=';')

    for row in reader:
        total_stock += int(row['stock'])
        if float(row['price']) > top['price']:
            top['name'] = row['name']
            top['price'] = float(row['price'])
        if int(row['stock']) < low['stock']:
            low['articlenum'] = int(row['articlenum'])
            low['stock'] = int(row['stock'])

    print('Het duurste artikel is %s en die kost %.2f Euro' % (top['name'], top['price']))
    print('Er zijn slechts %d exemplaren in voorraad van het product met nummer %d' % (low['stock'], low['articlenum']))
    print('In totaal hebben wij %d producten in ons magazijn liggen' % total_stock)
