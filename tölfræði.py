inputamount = int(raw_input())
import bisect

total = 0
amount = 0
min = 0
max = 0
amountofmin = 0
amountofmax = 0

hird = list()

def index(a, x, right=False):
    'Locate the leftmost value exactly equal to x'
    i = 0
    if not right:
        i = bisect.bisect_left(a, x)
    else:
        i = bisect.bisect_right(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

for i in range(inputamount):
    breyting = raw_input().split()
    tala = int(breyting[1])
    if breyting[0] == "A":
        if hird and tala <= hird[0]:
            hird.insert(0, tala)
        elif hird and tala >= hird[-1]:
            hird.append(tala)
        elif not hird:
            hird.append(tala)
        else:
            bisect.insort_left(hird, tala)
        amount += 1
        if amount == 1:
            total = tala
            min = tala
            max = tala
        else:
            total += tala
            if tala < min:
                min = tala
            if tala > max:
                max = tala
    else:
        amount -= 1
        total -= tala
        if amount < 0:
            amount = 0
        if amount == 0:
            hird = list()
            total = 0
        else:
            if tala == min:
                if hird[0] == tala:
                    hird.pop(0)
                    min = hird[0]
                else:
                    asd = index(hird, tala)
                    hird.pop(asd)
            elif tala == max:
                if hird[-1] == tala:
                    hird.pop()
                    max = hird[-1]
                else:
                    asd = index(hird, tala, True)
                    hird.pop(asd)
            else:
                asd = index(hird, tala)
                hird.pop(asd)

    if amount > 0:
        print str(min) + " " + str(max) + " " + str(float(total) / float(amount))
    else:
        print "-1 -1 -1"