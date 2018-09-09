import xmltodict

def processXML(filename):
    with open(filename) as XMLFile:
        return xmltodict.parse(XMLFile.read())

stations = processXML('stations.xml')

print('Dit zij nde codes en types van de %d stations:' % (len(stations)))
for station in stations['Stations']['Station']:
    print('{:5}- {}'.format(station['Code'], station['Type']))

print('\nDit zijn alle stations met een of meer synoniemen:')
for station in stations['Stations']['Station']:
    if station['Synoniemen']:
        print('{:5}- {}'.format(station['Code'], station['Synoniemen']))

print('\nDit is de lange naam van elk station:')
for station in stations['Stations']['Station']:
    print('{:5}- {}'.format(station['Code'], station['Namen']['Lang']))
