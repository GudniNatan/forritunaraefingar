import itertools
from random import shuffle

permutations = list()

for i in itertools.permutations(range(1, 7)):
    i = map(str, i)
    permutations.append("".join(i))

print(permutations)
print(len(permutations))
shuffle(permutations)
shortestSuper = [x for x in range(10000)]
a = list()
counter = 0
for asdasd in range(100000):
    shuffle(permutations)
    i = permutations
    counter += 1
    if counter % 10000 == 0:
        print counter
    superpermutation = i[0]
    for j in range(len(i)):
        k = i[j]
        if superpermutation.find(k) != -1:
            continue
        same = 0
        for n in range(len(k), 0, -1):
            if k[-n] == superpermutation[5-n]:
                same += 1
            else:
                break
        superpermutation += k[same:]
    if len(superpermutation) < len(shortestSuper):
        shortestSuper = superpermutation
        print(len(shortestSuper))
        print(shortestSuper)
        print("i: " + str(i))

print(shortestSuper)
print(len(shortestSuper))