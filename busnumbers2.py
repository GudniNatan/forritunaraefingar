from math import pow, floor

n = int(raw_input())

while n > 1728:
    count = 0
    a = n
    while a > n / 2:
        a = floor(a ** (1. / 3)) ** 3
        b = n - a + 1
        nearestCubeB = floor(b ** (1. / 3))
        if nearestCubeB ** 3 + a == n and a >= pow(nearestCubeB, 3):
            count += 1
            if count == 2:
                break
        a -= 1
    if count >= 2:
        print n
        break
    n -= 1
else:
    print "none"