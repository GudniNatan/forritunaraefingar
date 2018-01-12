n, m = map(int, raw_input().split())

ferdir = list()

for i in range(m):
    ferdir.append(map(int, raw_input().split()))

ferdir.sort()

ranges = list()

currentRange = [ferdir[0][0], ferdir[0][1]]

total = 0

for i in range(len(ferdir)):
    if ferdir[i][0] > currentRange[1]:
        ranges.append(currentRange)
        currentRange = ferdir[i]
    elif ferdir[i][1] > currentRange[1]:
        currentRange[1] = ferdir[i][1]

ranges.append(currentRange)

for r in ranges:
    total += r[1] - (r[0] - 1)

print total

if total > n / 2:
    print "The Mexicans took our jobs! Sad!"
else:
    print "The Mexicans are Lazy! Sad!"

