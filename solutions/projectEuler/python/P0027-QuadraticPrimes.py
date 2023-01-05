'''
Considering n^2 + an + b, |a| < 1000 and |b| <= 1000, starting with n=0,
Find a*b, for max number of primes created for consecutive n
Note: takes approx 10 minutes
'''

from datetime import datetime
import os

def distinctPowers():

    limit = 1000000
    primes = [1] * (limit+1)
    primes[0] = 0
    primes[1] = 0
    for i in range(2, limit):
        for j in range(i * 2, limit, i):
            primes[j] = 0

    # primeNumbers = []
    # for i in range(limit):
    #     if(primes[i] == 1):
    #         primeNumbers.append(i)

    ab = 0
    maxprimes = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            nprimes = 0
            for n in range(0,500):
                c = (n*n) + (a*n) + b
                #if c in primeNumbers:
                if primes[c] == 1:
                    nprimes += 1
                else:
                    print(a, b, n, nprimes, maxprimes, ab)
                    if nprimes > maxprimes:
                        ab = a * b
                        maxprimes = nprimes
                    break

    return ab
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(distinctPowers() ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )