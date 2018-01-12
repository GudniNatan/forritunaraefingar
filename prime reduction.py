def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n/3)
    for i in xrange(1,int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

primes = primes2(10000000)

#print len(primes)

while True:
    s = int(raw_input())
    if s == 4:
        break
    ogs = s
    counter = 0
    while True:
        original = s
        counter += 1
        factorSum = 0
        done = False
        fullyDone = False
        originalIsPrime = False
        for i in range(len(primes)):
            while not done:
                if s % primes[i] == 0 and s != primes[i]:
                    s /= primes[i]
                    factorSum += primes[i]
                else:
                    break
            if done and primes[i] > factorSum:
                break
            elif done and primes[i] == factorSum or primes[i] == original:
                if primes[i] == original:
                    originalIsPrime = True
                fullyDone = True
                break
            if s == primes[i]:
                factorSum += s
                done = True
        if originalIsPrime:
            print str(original) + " 1"
            break
        elif fullyDone or factorSum == 0:
            print str(factorSum) + " " + str(counter + 1)
            break
        else:
            s = factorSum
            #print s