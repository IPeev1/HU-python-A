import datetime
import csv

bestand = 'inloggers.csv'
while True:
    naam = input("Wat is je achternaam: ")

    if naam == 'einde':
        break

    voorl = input("Wat zijn je voorletters: ")
    gbdatum = input("Wat is je geboortedatum: ")
    email = input("Wat is je e-mail adres: ")

    with open(bestand, 'r', newline='\n') as ReadCSVFile:
        reader = csv.DictReader(ReadCSVFile, delimiter=';')
        bestaat = False
        for row in reader:
            if (row['geboortedatum'] == gbdatum) and (row['email'] == email):
                bestaat = True
                break
        if bestaat:
            print('De persoon bestaat')
        else:
            with open(bestand, 'a', newline='\n') as WriteCSVFile:
                writer = csv.writer(WriteCSVFile, delimiter=';')
                writer.writerow((
                    datetime.datetime.now().strftime('%a %d %b %Y') + ' at ' + datetime.datetime.now().strftime('%H:%M'),
                    voorl,
                    naam,
                    gbdatum,
                    email
                ))
