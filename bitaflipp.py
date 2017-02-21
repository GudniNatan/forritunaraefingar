#Ekki full lausn

def main():
    lengd = raw_input()
    band = raw_input()
    band = map(int, band.split())
    lengd = len(band)
    values = list()
    """totalSum = sum(band)
    if totalSum == 0:
        print lengd
        return
    if totalSum == lengd:
        print lengd-1
        return
    if totalSum == lengd-1:
        print lengd
        return """
    """for i in range(lengd):
        for j in range(1, lengd):
            value = sum(band[0:i]) + (len(band[i:i + j]) - sum(band[i:i + j])) + sum(band[i + j:lengd])
            if value > maxVal:
                maxVal = value"""
    summa = [0 for x in range(len(band))]
    for i in range(0, lengd):
        summa[i] = (0 if band[i] else 1) + summa[i - 1]
    #summa[0] = 0
    print summa
    maxVal = 0
    mn = 100000000000
    for j in range(lengd):
        mn = min(mn, summa[j - 1])
        maxVal  = max(maxVal, summa[j] - mn)
    if maxVal == -1:
        maxVal = 0
    print maxVal

main()

