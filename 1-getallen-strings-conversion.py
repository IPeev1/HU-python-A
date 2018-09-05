cijferICOR = int(input('Enter ICOR: '))
cijferPROG = int(input('Enter PROG: '))
cijferCSN = int(input('Enter CSN: '))
gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3
beloning = (cijferICOR + cijferPROG + cijferCSN) * 30
print('Mijn cijfer (gemiddeld een %d) leveren een beloning van €%d op!' % (gemiddelde, beloning))
