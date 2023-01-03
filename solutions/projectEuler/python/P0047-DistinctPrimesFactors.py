'''
Find first four consecutive numbers which have four distinct prime factors
Note: Takes 5 minutes to execute
'''

from datetime import datetime

def numOfPrimeFactors(num, primeNumbers):
    if num in primeNumbers:
        return 1

    numOfPrimeFactors = 0
    s = num / 2
    for i in primeNumbers:
        if i > s:
            break
        if (num % i == 0):
            numOfPrimeFactors += 1
            while (num % i == 0):
                num = num / i

    return numOfPrimeFactors 

def distinctPrimeFactors():
    
    limit = 1000000

    primes = [1] * (limit + 1)
    primes[0] = 0
    primes[1] = 0
    for i in range(2,limit):
        for j in range(2*i, limit, i):
            primes[j] = 0

    primeNumbers = [] #list of actual prime numbers
    for i in range(limit):
        if primes[i] == 1:
            primeNumbers.append(i)
        
    primeFactors = dict()
    for i in range(1,limit):
        primeFactors[i] = numOfPrimeFactors(i, primeNumbers)
        print(i, primeFactors[i])
        
        if primeFactors[i] == 4 and primeFactors[i-1] == 4 and primeFactors[i-2] == 4 and primeFactors[i-3] == 4:
                print(i, i-1, i-2, i-3)
                return i-3
    
    return 0
    
if __name__ == '__main__':

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(distinctPrimeFactors() ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )