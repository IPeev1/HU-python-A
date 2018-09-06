def seizoen(maand):
    if maand < 1 or maand > 12:
        print('Geen geldig nummer')
    else:
        if maand >= 3 and maand <= 5:
            return 'lente'
        elif maand >= 6 and maand <= 8:
            return 'zomer'
        elif maand >= 9 and maand <= 11:
            return 'herfst'
        else:
            return 'winter'

for i in range(1, 13):
    print('%d, %s' % (i, seizoen(i)))