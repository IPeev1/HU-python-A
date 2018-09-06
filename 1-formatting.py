def convert(c):
    return (c * 1.8) + 32

def table():
    print('{:2}{:8}{}'.format('', 'F', 'C'))
    for deg in range(-30, 50, 10):
        print('{:5.1f}{:8.1f}'.format(convert(deg), deg))

table()