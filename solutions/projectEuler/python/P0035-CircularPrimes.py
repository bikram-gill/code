'''
Find total number of primes below n, whose all rotations are also prime.
'''

from datetime import datetime
import os

def circularPrimes(limit):

    isPrime = [1] * (limit+1)
    
    isPrime[0] = 0
    isPrime[1] = 0

    #prepare prime array
    for i in range(2,limit+1):
        for j in range(i*2, limit+1, i):
            isPrime[j] = 0

    s = set() #collection of unique circular primes

    #rotate each number from 2-limit to check for prime
    for j in range(2,limit+1):
        #include single digits in set
        if(len(str(j)) == 1 and isPrime[j] == 1):
            s.add(j);
        
        #test for all possible rotations
        isCircular = True
        num = str(j)
        for k in range(len(str(j))):
            new = num[k:] + num[:k]
            if(isPrime[int(new)] == 0):
                isCircular = False
                break
        
        if(isCircular):
            s.add(j)

    print(s)

    return len(s)
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    limit = int(input('What is the highest limit to find circular primes (E.g. 1000000): '))

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(circularPrimes(limit) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )