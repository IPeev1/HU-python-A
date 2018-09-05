import sys

age = int(input('Geef je leeftijd: '))
passport = input('Nederlands paspoort (ja/nee): ').lower()

if age >= 18 and passport == 'ja':
    print('Gefeliciteerd, je mag stemmen!')
    sys.exit(0)
else:
    print('Jammer, je mag niet stemmen')
    sys.exit(0)