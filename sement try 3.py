from sys import exit

n, m = map(int, raw_input().split())

num = [list() for x in range(1000000)]

normalList = list()
normalSet = list()
nope = False

mid = m / 2
midBool = False
mc = 0
if m % 2 == 0:
    midBool = True

for i in xrange(n):
    a = int(raw_input())
    if midBool and a == mid:
        mc += 1
        if mc > 1:
            midBool = False
    normalList.append(a)
    if a > 1000000000:
        nope = True
    if not nope and a not in num[a / 100000]:
        num[a / 100000].append(a)

if mc > 1:
    print mid, mid
    exit()

if not nope:
    for g in xrange(len(num)):
        for u in xrange(len(num[g])):
            i = num[g][u]
            a = m - i
            if a in num[a / 100000] and a != i:
                print a, i
                exit()

else:
    normalSet = list(set(normalList))
    l = len(normalSet)
    for x in xrange(l):
        for y in xrange(x, l):
            if normalSet[x] + normalSet[y] == m:
                print normalSet[x], normalSet[y]
                exit()

print "Neibb"