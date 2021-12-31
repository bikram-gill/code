'''
Find first triangular number to have N divisors

NOTE: Calculation of primes takes sometime, after that the operation is faster
'''

from datetime import datetime

def findPrimes(maxNumber):

    start = datetime.now().strftime("%H:%M:%S")

    primes = []
    
    #initialize prime number array, number corresponding to index is a prime if value is True (except first 2)
    primeArray = [True for i in range(maxNumber + 1)] 
    number = 2
    while True:
        
        #If current number of prime, mark its multiples out of the primeArray
        if primeArray[number]:
            primes.append(number)
            
            if number * 2 > maxNumber:
                number += 1
                continue

            for counter in range(number * 2, maxNumber+1, number):
                #Number corresponding to this index is not prime
                if primeArray[counter]:
                    primeArray[counter] = False
        
        number += 1
        if number > maxNumber:
            break
    
    
    end = datetime.now().strftime("%H:%M:%S")

    print( 'Prime calculation, start and end time: ', start, ' ', end )

    return primes


'''
Using standard formula for divisor calculation.
'''
def findDivisors(number, primes):

    divisors = 1

    for i in primes:
        count = 0
        while number % i == 0:
            number /= i
            count += 1
        
        if count > 0:
            divisors *= (count + 1)

        if i > number:
            break 

    return divisors


def highlyDivisibleTriangularNumber(divisors):

    number = 1
    i = 1
    
    if divisors > 100:
        primes = findPrimes(100000000) #arbitrary limit based on testing for 500 divisors
    else:
        primes = findPrimes(100000)

    #find triangular numbers
    while True:
        if divisors < findDivisors(number, primes):
            return number

        i += 1
        number += i


if __name__ == '__main__':

    divisors = int(input('Number of divisors for the triangular number (E.g. 500): ') )

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(highlyDivisibleTriangularNumber(divisors) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )