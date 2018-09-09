def inlezen_beginstation(stations):
    while True:
        beginstation = input('Beginstation: ')

        if beginstation in stations:
            return beginstation
        else:
            print('Dit station is niet aanwezig in het traject')

def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input('Eindstation: ')

        if eindstation in stations:
            if stations.index(beginstation) < stations.index(eindstation):
                return eindstation
            elif stations.index(beginstation) == stations.index(eindstation):
                print('Gefeliciteerd, je bent al op het station')
            else:
                print('Dit station komt voor het geselecteerde beginstation')
        else:
            print('Dit station is niet aanwezig in het traject')

def omroepen_reis(stations, beginstation, eindstation):
    beginIdx = stations.index(beginstation)
    eindIdx = stations.index(eindstation)

    print('\nHet beginstation %s is het %de station in het traject' % (beginstation, beginIdx + 1))
    print('Het eindstation %s is het %de station in het traject' % (eindstation, eindIdx + 1))
    print('De afstand bedraagt %d station(s)' % (eindIdx - beginIdx))
    print('De prijs van het kaartje is %d euro\n' % ((eindIdx - beginIdx) * 5))

    print('Jij stapt in de trein in: %s' % beginstation)
    for i in range(beginIdx + 1, eindIdx):
        print(' - %s' % stations[i])
    print('Jij stapt uit in: %s' % eindstation)

stations = [
    'Schagen',
    'Heerhugowaard',
    'Alkmaar',
    'Castricum',
    'Zaandam',
    'Amsterdam Sloterdijk',
    'Amsterdam Centraal',
    'Amsterdam Amstel',
    'Utrecht Centraal',
    '\'s-Hertogenbosch',
    'Eindhoven',
    'Weert',
    'Roermond',
    'Sittard',
    'Maastricht'
]
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
