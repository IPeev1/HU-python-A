f = open('kaartnummers.txt', 'r')
lines = f.readlines()
f.close()

nums = []

for line in lines:
    nums.append(line.split(', ')[0])
maxNum = max(nums)

print('Deze file telt %d regels' % len(lines))
print('Het grootste kaartnummer is: %s en dat staat op regel %d' % (maxNum, nums.index(maxNum) + 1))
