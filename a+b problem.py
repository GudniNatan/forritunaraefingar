from collections import Counter

n = int(raw_input())

numbers = map(int, raw_input().split())

numbersum = sum(numbers)
totalways = 0

totalRepeats = 0
numberOfZeros = 0
for k, v in Counter(numbers).most_common(3):
    if v == 0:
        break
    if k == 0:
       numberOfZeros = v
    totalRepeats += v - 1
#print totalRepeats
for n in range(len(numbers)):
    if numbers[n] == 0:
        totalways += (totalRepeats - (1 - numberOfZeros % 2)) * 2
        """for k, v in Counter(numbers).most_common(3):
            if v == 0:
                break
            if k == 0:
                numberOfZeros = v
            totalRepeats += v"""
    elif numbersum % numbers[n] == 0:
        totalways += 2

print totalways