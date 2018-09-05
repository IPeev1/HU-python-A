def som(getal1, getal2, getal3):
    return getal1 + getal2 + getal3
print(som(1, 2, 3))

# betere oplossing:
# def som(*args):
#     return sum(args)
# dit maakt de functie 'som' eigenlijk onnodig
# sum kan gewoon geroepen worden met als eerste parameter een list of tuple van alle getallen
