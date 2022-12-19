'''
What is the largest n-digit pandigital prime that exists?
'''

from datetime import datetime
import os

def pandigitalPrime(limit):

    #generate prime array
    max = limit
    primes = [1] * max
    primes[0] = 0
    primes[1] = 0
    for i in range(2, max):
        for j in range(i*2, max, i):
            primes[j] = 0

    pandigital = '123456789'
    for k in range(max-1,0,-1):
        if primes[k]:
            s = str(k)
            if ''.join(sorted(s)) == pandigital[:len(s)]:
                return k

    return 0

if __name__ == '__main__':
    
    print(os.getcwd())
    
    limit = int(input('What is the highest limit for pandigital prime (E.g. 10000000): '))

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(pandigitalPrime(limit) ) )
    
    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )