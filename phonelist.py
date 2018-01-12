t = int(raw_input())
for case in xrange(t):
    n = int(raw_input())
    numbers = list()

    for i in xrange(n):
        numbers.append(raw_input())

    ln = "-"
    for number in sorted(numbers):
        if ln == number[:len(ln)]:
            print "NO"
            break
        ln = number
    else:
        print "YES"