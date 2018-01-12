cases = int(raw_input())
snowflakes = [False for i in xrange(500000)]
all = list()
for a in range(cases):
    for i in all:
        snowflakes[i] = False
    maxtotal = 0
    row = list()
    all = list()
    n = int(raw_input())
    for j in xrange(n):
        inp = int(raw_input())
        if snowflakes[inp] == False:
            snowflakes[inp] = True
            row.append(inp)
            all.append(inp)
        else:
            maxtotal = max(maxtotal, len(row))
            row.append(inp)
            for i in range(len(row)):
                if row[i] == inp:
                    row = row[i + 1:]
                    break
                snowflakes[row[i]] = False
    print max(maxtotal, len(row))