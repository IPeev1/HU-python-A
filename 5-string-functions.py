def gemiddelde():
    woorden = input('Vul een zin in: ').split(' ')
    som = 0
    for woord in woorden:
        som += len(woord)
    print('Gemiddelde aantal karakters per woord: %.1f' % (som / len(woorden)))
gemiddelde()
