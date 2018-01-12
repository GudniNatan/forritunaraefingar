def main():

    n, m = map(int, raw_input().split())
    oddaPokar = list()
    slettirPokar = list()
    for i in range(n):
        p = int(raw_input())
        if p % 2:
            if p not in oddaPokar and p < m:
                oddaPokar.append(p)
        else:
            if p not in slettirPokar and p < m:
                slettirPokar.append(p)

    oddaPokar.sort()
    slettirPokar.sort()

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