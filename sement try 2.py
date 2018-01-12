def main():

    n, m = map(int, raw_input().split())
    npokar = [list() for x in range(100)]
    oddaPokar = list()
    slettirPokar = list()
    for i in range(n):
        p = int(raw_input())
        if p not in npokar[p % 100] and p < m:
            npokar[p % 100].append(p)
        if p % 2:
            if p not in oddaPokar and p < m:
                oddaPokar.append(p)
        else:
            if p not in slettirPokar and p < m:
                slettirPokar.append(p)
    for i in range(100):
        if m % 100 == i:
            pokar = npokar[p % 100]
            for i in xrange(len(pokar)):
                for j in xrange(i, len(pokar)):
                    if pokar[i] + pokar[j] == m:
                        print pokar[i], pokar[j]
                        return
    slettirPokar.sort()
    oddaPokar.sort()
    if m % 2 == 1:
        for i in xrange(len(slettirPokar)):
            for j in xrange(len(oddaPokar) - 1, 0, -1):
                if slettirPokar[i] + oddaPokar[j] == m:
                    print slettirPokar[i], oddaPokar[j]
                    return
        else:
            print "Neibb"
    else:
        for i in xrange(len(slettirPokar)):
            for j in xrange(len(slettirPokar) - 1, i, -1):
                if slettirPokar[i] + slettirPokar[j] == m:
                    print slettirPokar[i], slettirPokar[j]
                    return
        for i in xrange(len(oddaPokar)):
            for j in xrange(len(oddaPokar) - 1, i, -1):
                if oddaPokar[i] + oddaPokar[j] == m:
                    print oddaPokar[i], oddaPokar[j]
                    return
        print "Neibb"
main()