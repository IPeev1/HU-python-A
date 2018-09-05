s = 'Guido van Rossum heeft programmeertaal Python bedacht.'.lower()

for c in s:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        print(c)

# betere manier om te tellen hoeveel er van ieder klinker is:
# *map(s.count, 'aeiou')
