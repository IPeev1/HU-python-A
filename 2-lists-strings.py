num_strings = 10
strings = []
new_strings = []

while num_strings != 0:
    strings.append(input('Geef een string (%d): ' % num_strings))
    num_strings -= 1

for i in range(len(strings)):
    if len(strings[i]) == 4:
        new_strings.append(strings[i])
print(new_strings)