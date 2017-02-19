#Ekki full lausn
amount = int(raw_input())
requests = list()
possible = True
for i in range(amount):
    req = raw_input().split()
    requests.append([int(req[0]), int(req[1])])

tshrits = raw_input().split()
totalts = dict()
for i in range(amount):
    size = int(tshrits[i])
    if totalts.has_key(size):
        totalts[size] += 1
    else:
        totalts[size] = 1

for i in range(amount):
    maxt = -1
    maxtnum = -1
    for j in range(requests[i][0], requests[i][1] + 1):
        if totalts.has_key(j) and totalts[j] > maxtnum and totalts[j] > 0:
            maxt = j
            maxtnum = totalts[j]
    if maxt == -1 or maxtnum == -1:
        possible = False
        break
    else:
        totalts[maxt] -= 1


if not possible:
    print "Neibb"
else:
    print "Jebb"