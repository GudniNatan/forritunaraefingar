"""from itertools import permutations
import math
import random
n = int(input())
points = []
for i in range(n):
    points.append(list(map(float, input().split())))

points.sort()
print(points)

length = 100000000
for i in range(10000000000000):
    dist = 0
    p = list(points)
    random.shuffle(p)
    for i in range(1, len(p)):
        dist += math.hypot(p[i][0] - p[i - 1][0], p[i][1] - p[i - 1][1])
    if dist < length:
        length = dist
        print(dist)
        print(p)
"""
n, q = list(map(int, input().split()))
tour = ['0']
for i in range(n):
    tour.append(input().split()[1])

print(" ".join(tour))