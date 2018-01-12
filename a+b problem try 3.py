n = int(raw_input())
i = map(int, raw_input().split())
s = sum(i)
c = 0
for x in i:
    if s % x == 0:
        c += 2
    print s / x

print c