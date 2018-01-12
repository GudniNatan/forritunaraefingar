n = int(raw_input())
m = int(raw_input())

stig = [0 for x in xrange(n)]
lid = raw_input().split()

for k in xrange(m):
    s = map(int, raw_input().split())
    for i in range(n):
        stig[i] += s[i]

print lid[stig.index(max(stig))]