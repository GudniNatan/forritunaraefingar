n = int(raw_input())
m = int(raw_input())

fjperstofa = m / n

afgangur = m % n

if afgangur:
    fjperstofa += 1

asd = ["*" for x in range(fjperstofa)]

strengur = "".join(asd)

for line in xrange(n):
    print strengur
    if afgangur:
        afgangur -= 1
        if afgangur == 0:
            asd.pop()
            strengur = "".join(asd)