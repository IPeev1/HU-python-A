invoer = '5-9-7-1-7-8-3-2-4-8-7-9'
getallen = [int(i) for i in invoer.split('-')]
getallen.sort()
print('Gesorteerde list van ints: [%s]' % ', '.join([str(i) for i in getallen]))
print('Grootste getal: %d en Kleinste getal: %d' % (max(getallen), min(getallen)))
print('Aantal getallen: %d en Som van de getallen: %d' % (len(getallen), sum(getallen)))
print('Gemiddelde: %f' % (sum(getallen) / len(getallen)))