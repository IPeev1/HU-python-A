def namen():
    names = {}
    while True:
        name_in = input('Volgende naam: ')
        if len(name_in) == 0:
            for name, count in names.items():
                if count == 1:
                    print('Er is %d student met de naam %s' % (count, name))
                elif count > 1:
                    print('Er zijn %d studenten met de naam %s' % (count, name))
            break
        else:
            names_exist = names.keys()
            if name_in in names_exist:
                names[name_in] += 1
            else:
                names[name_in] = 1
namen()
