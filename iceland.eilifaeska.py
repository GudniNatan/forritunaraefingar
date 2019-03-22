n = int(input())
cups = list(map(int, input().split()))
log = list()
counter = 0

while(max(cups) != min(cups)):
    counter += 1
    maxIndex = cups.index(max(cups))
    minIndex = cups.index(min(cups))

    log.append("%d %d" % (maxIndex + 1, minIndex + 1))

    cups[maxIndex] = (cups[maxIndex] + cups[minIndex]) / 2
    cups[minIndex] = cups[maxIndex]

if counter > 20:
    print(-1)
else:
    print(len(log))
    for s in log:
        print(s)