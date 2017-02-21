import itertools
operations = {"*", "+", "-", "/"}

n = int(raw_input())
for i in range(n):
    tala = int(raw_input())
    for i in itertools.product(operations, repeat=3):
        if eval("4 " + i[0] + " 4 " + i[1] + " 4 " + i[2] + " 4") == tala:
            print "4 " + i[0] + " 4 " + i[1] + " 4 " + i[2] + " 4 = " + str(tala)
            break
    else:
        print "no solution"