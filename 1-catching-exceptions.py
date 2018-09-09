while True:
    try:
        aantal = int(input('Aantal mensen: '))
        if aantal < 0:
            raise ValueError('Negatieve getallen zijn niet toegestaan!')
        print('Prijs per persoon: %.2f' % (4356.0 / aantal))
    except TypeError:
        print('Gebruik cijfers voor het invoeren van het aantal!')
    except ValueError:
        print('Het aantal mensen moet een getal zijn')
    except ZeroDivisionError:
        print('Delen door nul kan niet!')