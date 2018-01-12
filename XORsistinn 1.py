n = int(raw_input())


def get_xor_number(i):
    numbers = [i, 1, i + 1, 0]
    return numbers[i % 4]

xor = get_xor_number(n)

if xor == 0:
    print "Enginn"
elif xor > n:
    print "Gunnar"
else:
    print xor