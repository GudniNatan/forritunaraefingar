desired = [1, 1, 2, 2, 2, 8]

asd = map(int, raw_input().split())

for i in range(len(desired)):
    desired[i] = str(desired[i] - asd[i])

print " ".join(desired)