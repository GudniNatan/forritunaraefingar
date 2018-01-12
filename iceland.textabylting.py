from itertools import izip_longest

n = int(raw_input())
strengir = list()
joinIt = "".join

for i in range(n):
    strengir.append(raw_input())

for x in izip_longest(*strengir, fillvalue=" "):
    print joinIt(x)