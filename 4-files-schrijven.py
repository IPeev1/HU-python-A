import datetime

names = ['Miranda', 'Piet', 'Sacha', 'Karel', 'Kemal']
f = open('hardlopers.txt', 'a')

for name in names:
    f.write('{}, {}\n'.format(datetime.datetime.today().strftime('%a %d %b %Y, %H:%M:%S'), name))
f.close()

f = open('hardlopers.txt', 'r')

for line in f.readlines():
    print(line)
f.close()