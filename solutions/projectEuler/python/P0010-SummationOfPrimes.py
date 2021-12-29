'''
Find sum of all primes below N.
'''

from datetime import datetime
import math
import itertools


def summationOfPrimes(N):
    sum = 0
    
    #initialize prime number array, number corresponding to index is a prime if value is True
    primeArray = [True for i in range(N+1)] 
    number = 2
    while True:
        
        #If current number of prime, mark its multiples out of the primeArray
        if primeArray[number]:
            sum += number
            #print(sum)
            if number * 2 > N:
                number += 1
                continue

            for counter in range(number * 2, N+1, number):
                #Number corresponding to this index is not prime
                if primeArray[counter]:
                    primeArray[counter] = False
        
        number += 1
        if number > N:
            break
    
    return sum
    
if __name__ == '__main__':
    N = int (input('Input upper bound number to find sum of all primes (E.g. 2000000): ') )
    
    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(summationOfPrimes( N) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )