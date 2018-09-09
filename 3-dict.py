students = {
    'Tim': 7.0,
    'Tom': 9.4,
    'Paul': 6.6,
    'Stefan': 4.8,
    'Rene': 6.7,
    'Ruben': 8.4,
    'Jean-Paul': 9.8,
    'Robert': 9.3,
}

for name, grade in students.items():
    if grade >= 9.0:
        print('%s: %.1f' % (name, grade))