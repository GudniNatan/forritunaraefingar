n = 542
tolur = [True for x in xrange(n)]
for i in xrange(2, int(n**0.5) + 1):
    if tolur[i]:
        for j in range(n):
            tala = (i ** 2) + (j * i)
            if tala >= n:
                break
            tolur[tala] = False

for i in xrange(2, n):
    if tolur[i]:
        print i