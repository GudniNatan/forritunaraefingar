import math

for i in xrange(1, 101):
    number = str(int(math.pow(2, i)))
    if len(number) % 2 == 0:
        halfnumber = number[:len(number) / 2]
        finalnumber = halfnumber + halfnumber[::-1]
        if int(finalnumber) > int(number):
            halfnumber = str(int(halfnumber) - 1)
            finalnumber = halfnumber + halfnumber[::-1]
    else:
        halfnumber = number[:(len(number) -1) / 2]
        finalnumber = halfnumber + number[(len(number)) / 2] + halfnumber[::-1]
        if int(finalnumber) > int(number):
            finalnumber = halfnumber + str(int(number[(len(number)) / 2]) - 1) + halfnumber[::-1]
            if int(number[(len(number)) / 2]) == 0:
                halfnumber = str(int(halfnumber) - 1)
                finalnumber = halfnumber + "9" + halfnumber[::-1]

    print str(i) + " " + finalnumber