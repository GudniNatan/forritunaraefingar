n, m, k = map(int, raw_input().split())

a = list()

for i in range(k):
    x, y = map(int, raw_input().split())
    a.append(x - y)

print len(set(a))