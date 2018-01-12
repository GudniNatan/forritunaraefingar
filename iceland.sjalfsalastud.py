(fj, t, f, h) = map(int, raw_input().split())

p = 0

for x in range(fj):
    if h:
        p += 1
        h -= 1
        t += 2
    elif f and t >= 3 and f / 2 < fj - (x + 1):
        p += 4
        f -= 1
        t -= 3
    elif f >= 2:
        p += 2
        f -= 2
        t += 2
    elif f and t >= 3:
        p += 4
        f -= 1
        t -= 3
    elif t >= 8:
        p += 8
        t -= 8

print p