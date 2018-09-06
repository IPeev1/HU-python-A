import os, time, sys

def toon_aantal_kluizen_vrij():
    print('[Aantal kluizen]')
    f = open('kluizen.txt', 'r')
    length = len(f.readlines())
    f.close()

    if length >= 12:
        print('Helaas zijn er geen kluizen beschikbaar')
    else:
        print('Er zijn %d kluizen beschikbaar' % (12 - length))
    time.sleep(3)

def nieuw_kluis():
    print('[Nieuwe kluis]')
    keuzes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    f = open('kluizen.txt', 'r')
    kluizen = f.readlines()
    f.close()

    for kluis in kluizen:
        num = int(kluis.split(';')[0])
        if num in keuzes:
            keuzes.remove(num)

    if len(keuzes) > 0:
        code = input('Voer uw code in: ')
        if len(code) >= 4:
            f = open('kluizen.txt', 'a')
            f.write('%d;%s\n' % (keuzes[0], code))
            f.close()
            print('Uw kluisnummer is: %d, met code: %s' % (keuzes[0], code))
        else:
            print('Uw code is niet lang genoeg')
            time.sleep(3)
    else:
        print('Helaas zijn er geen kluizen beschikbaar')
    time.sleep(3)

def kluis_openen():
    print('[Kluis openen]')
    try:
        kluis_num = int(input('Kluisnummer: '))
    except ValueError:
        print('Het kluisnummer moet een getal zijn!')
        time.sleep(3)
        return
    kluis_code = input('Kluiscode: ')
    f = open('kluizen.txt', 'r')
    kluizen = f.readlines()
    f.close()

    for kluis in kluizen:
        kluis_info = kluis.split(';')
        if (int(kluis_info[0]) == kluis_num) and (kluis_info[1].strip() == kluis_code):
            print('Uw gegevens zijn correct!')
            time.sleep(3)
            return
    print('Helaas zijn uw gegevens niet correct')
    time.sleep(3)

def kluis_teruggeven():
    print('[Kluis teruggeven]')
    try:
        kluis_num = int(input('Kluisnummer: '))
    except ValueError:
        print('Het kluisnummer moet een getal zijn!')
        time.sleep(3)
        return
    kluis_code = input('Kluiscode: ')

    f = open('kluizen.txt', 'r')
    kluizen = f.readlines()
    f.close()

    kluis_bestaat = False

    for kluis in kluizen:
        kluis_info = kluis.split(';')
        if (int(kluis_info[0]) == kluis_num) and (kluis_info[1].strip() == kluis_code):
            kluis_bestaat = True

    if kluis_bestaat:
        f = open('kluizen.txt', 'w')
        for kluis in kluizen:
            kluis_info = kluis.split(';')
            if (int(kluis_info[0]) != kluis_num):
                f.write(kluis)
        f.close()
        print('Uw kluis is teruggegeven!')
        time.sleep(3)
    else:
        print('Uw kluis is niet gevonden')
        time.sleep(3)

def clearterm():
    os.system('cls' if os.name == 'nt' else 'clear')

def error():
    clearterm()
    print('Ongeldige invoer!')
    time.sleep(1)

while True:
    clearterm()
    print('''1: ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug\n5: ik wil stoppen''')
    choice = 0

    try:
        choice = int(input('> '))
    except ValueError:
        error()
        continue

    if (choice < 1 or choice > 5):
        error()
        continue
    else:
        clearterm()
        if choice == 1:
            toon_aantal_kluizen_vrij()
        elif choice == 2:
            nieuw_kluis()
        elif choice == 3:
            kluis_openen()
        elif choice == 4:
            kluis_teruggeven()
        elif choice == 5:
            clearterm()
            print('Tot ziens!')
            time.sleep(1)
            sys.exit(0)
