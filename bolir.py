from Queue import PriorityQueue
amount = int(raw_input())
requests = list()
possible = True
for i in range(amount):
    req = raw_input().split()
    requests.append((int(req[0]), 1, int(req[1])))

tshrits = raw_input().split()
totalts = list()
for i in range(amount):
    size = int(tshrits[i])
    totalts.append((size, 2, 0))

tsandrequests = list()
tsandrequests.extend(totalts)
tsandrequests.extend(requests)
tsandrequests.sort()
queue = PriorityQueue()

def coolDude():
    for i in range(len(tsandrequests)):
        if tsandrequests[i][1] == 1:
            queue.put(tsandrequests[i][2])
            continue
        if not queue.empty():
            bound = queue.get()
            if bound < tsandrequests[i][0]:
                return False
        else:
            return False
    return True


if coolDude():
    print "Jebb"
else:
    print "Neibb"