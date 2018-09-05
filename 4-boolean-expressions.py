a = 6
b = 7
c = (a + b) / 2
voornaam = 'Ivan'
tussenvoegsel = 'Ivanov'
achternaam = 'Peev'
mijnnaam = '%s %s %s' % (voornaam, tussenvoegsel, achternaam)

print(75 > a)
print(75 < b)

print((len(voornaam) + len(tussenvoegsel) + len(achternaam)) == len(mijnnaam))
print(len(mijnnaam) > 5 * len(tussenvoegsel))
print(tussenvoegsel in achternaam)