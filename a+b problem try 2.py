not_used = int(raw_input())
i = (map(int, raw_input().split()))
l = [0 for x in range(100001)]

c = 0

for x in i:
    l[x + 50000] += 1

i = list(set(i))
n = len(i)


for x in xrange(n):
    for y in xrange(x + 1, n):
        num = i[x] + i[y]
        if not -50000 <= num <= 50000:
            continue
        index = num + 50000
        if l[index] > 0:
            if i[x] == 0 or i[y] == 0:
                c += l[i[x] + 50000] * l[i[y] + 50000] * (l[index] - 1) * 2
            else:
                c += l[i[x] + 50000] * l[i[y] + 50000] * l[index] * 2
for x in xrange(n):
    if l[i[x] + 50000] >= 2:
        num = i[x] + i[x]
        index = num + 50000
        if l[index] > 0:
            if num == i[x] and l[index] >= 3:
                c += (l[index] - 2) * (l[index] - 1) * l[index]
            else:
                c += l[i[x] + 50000] * (l[i[x] + 50000] - 1) * l[index]
print c
