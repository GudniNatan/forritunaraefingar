import math

def main():

    n = int(raw_input())

    for bla in xrange(1, 100000):
        i = bla * 1000000000
        if i * math.log10(i) / 1000000 > n:
            for ra in xrange(1, 1000000000, 10000):
                j = (ra + i) - 1000000000
                if j * math.log10(j) / 1000000 > n:
                    for asd in range(j - 10000, j):
                        if asd * math.log10(asd) / 1000000 > n:
                            print asd - 1
                            return

main()