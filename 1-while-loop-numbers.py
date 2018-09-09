nums = []

while True:
    getal = int(input('Geef een getal: '))
    if getal == 0:
        break
    nums.append(getal)
print('Er zijn %d getallen ingevoerd, de som is: %d' % (len(nums), sum(nums)))
