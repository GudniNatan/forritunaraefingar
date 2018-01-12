n = int(raw_input())

verkStafir = dict()
verk = list()

for i in range(n):
    v = raw_input()
    try:
        if v not in verkStafir[v[:2]]:
            verkStafir[v[:2]] = v
            verk.append(v)
    except KeyError:
        verkStafir[v[:2]] = v
        verk.append(v)

for v in verk:
    print v