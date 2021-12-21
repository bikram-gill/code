'''
Find larget prime factor of given input number.
'''
import math
from datetime import datetime

def largestPrimeFactor( num ):
    
    max_root = int(math.sqrt(num))

    factors = []
    primes = []

    #Starting with 2, find primes and check whether they are a multiple of 
    #given input. Divide number with the multiple, until num reduces to 
    #less than the prime counter or end of counter

    for i in range(2, max_root + 1):
        if (i >= num):
            break

        if not any([ i % prime == 0 for prime in primes ]):
            primes.append(i)        #number is a prime
            
            if num % i == 0:
                factors.append(i)   #prime is a factor
        
                while True:
                    if (num % i != 0):
                        break
                    num = num / i   #reduce number using the factor
                    factors.append(i)

    #append final factor (prime)
    if num != 1:
        factors.append(num)

    print(factors)

    return sorted(factors)[-1]

if __name__ == '__main__':
    max = int( input('Input upper bound (e.g. 600851475143): ') )
    
    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(largestPrimeFactor( max ) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )