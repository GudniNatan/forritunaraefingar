def sum_digits(n):
   r = 0
   while n:
       r += n % 10
       n //= 10
   return r

while True:
    number = int(raw_input())
    if number == 0:
        break
    sumOfDigits = sum_digits(number)
    for i in xrange(11, 100):
        if sum_digits(i * number) == sumOfDigits:
            print i
            break
    else:
        print 100