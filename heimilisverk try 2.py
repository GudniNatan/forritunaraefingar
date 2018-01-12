n = int(raw_input())

verk = list()

for i in range(n):
    verk.append((raw_input(), i))

verk.sort()

verkTil = list()

seinastaVerk = verk[0]
verkTil.append((seinastaVerk[1], seinastaVerk[0]))

for v in verk:
    if v[0] != seinastaVerk[0]:
        verkTil.append((v[1], v[0]))

    seinastaVerk = v

verkTil.sort()

for v in verkTil:
    print v[1]