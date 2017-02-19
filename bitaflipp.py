#Ekki full lausn

def main():
    lengd = raw_input()
    band = raw_input()
    band = map(int, band.split())
    lengd = len(band)
    values = list()
    maxVal = -1
    totalSum = sum(band)
    if totalSum == 0:
        print lengd
        return
    if totalSum == lengd:
        print lengd-1
        return
    if totalSum == lengd-1:
        print lengd
        return
    for i in range(lengd):
        for j in range(1, lengd):
            value = sum(band[0:i]) + (len(band[i:i + j]) - sum(band[i:i + j])) + sum(band[i + j:lengd])
            if value > maxVal:
                maxVal = value
    if maxVal == -1:
        maxVal = 0
    print maxVal

main()

