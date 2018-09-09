def ticker(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    symbols = {}

    for line in lines:
        info = line.split(':')
        symbols[info[0]] = info[1].rstrip()
    return symbols

symbols = ticker('ticker-symbol.txt')

compName = input('Enter Company name: ')
print('Ticker symbol: %s\n' % (symbols[compName]))

tickSym = input('Enter Ticker: ')
compNames = symbols.keys()

for comp in compNames:
    symbols[comp] = symbols[comp]
    if symbols[comp] == tickSym:
        print(comp)
        break
