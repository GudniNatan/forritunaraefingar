number = int(raw_input())

if number > 0:
    finalnumber = (number * (number + 1)) / 2
    print finalnumber
else:
    number = -number
print -((number * (number + 1)) / 2) + 1