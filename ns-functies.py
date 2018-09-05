def standaardtarief(afstandKM):
    afstand = afstandKM if afstandKM > 0 else 0
    if afstand > 50:
        return 15.0 + (afstand * 0.60)
    else:
        return afstand * 0.80

def ritprijs(leeftijd, weekendrit, afstandKM):
    tarief = standaardtarief(afstandKM)

    if weekendrit:
        if leeftijd < 12 or leeftijd >= 65:
            return (tarief / 100) * (100 - 35)  # 35% korting
        else:
            return (tarief / 100) * (100 - 40)  # 40% korting
    else:
        if leeftijd < 12 or leeftijd >= 65:
            return (tarief / 100) * (100 - 30)  # 30% korting
        else:
            return tarief  # geen korting


print('%.2f' % ritprijs(11, True, -2))
print('%.2f' % ritprijs(11, True, 20))
print('%.2f' % ritprijs(11, True, 52))

print('-----------------')

print('%.2f' % ritprijs(12, True, -2))
print('%.2f' % ritprijs(12, True, 20))
print('%.2f' % ritprijs(12, True, 52))

print('-----------------')

print('%.2f' % ritprijs(64, True, -2))
print('%.2f' % ritprijs(64, True, 20))
print('%.2f' % ritprijs(64, True, 52))

print('-----------------')

print('%.2f' % ritprijs(65, True, -2))
print('%.2f' % ritprijs(65, True, 20))
print('%.2f' % ritprijs(65, True, 52))

print('-----------------')

print('%.2f' % ritprijs(11, False, -2))
print('%.2f' % ritprijs(11, False, 20))
print('%.2f' % ritprijs(11, False, 52))

print('-----------------')

print('%.2f' % ritprijs(12, False, -2))
print('%.2f' % ritprijs(12, False, 20))
print('%.2f' % ritprijs(12, False, 52))

print('-----------------')

print('%.2f' % ritprijs(64, False, -2))
print('%.2f' % ritprijs(64, False, 20))
print('%.2f' % ritprijs(64, False, 52))

print('-----------------')

print('%.2f' % ritprijs(65, False, -2))
print('%.2f' % ritprijs(65, False, 20))
print('%.2f' % ritprijs(65, False, 52))
