'''
Find Nth prime number.

NOTE: Program takes around 3.5 minutes for numbers over 10000
'''

from datetime import datetime

def nthPrime(n):
    
    primes = [2]    #first prime
    counter = 1     #1st prime counter
    number = 3      #number just higher than 1st prime to start calculation

    while counter < n:
        if all(number % i != 0 for i in primes):
            primes.append(number)
            counter += 1
            #print(counter, ' ', number)
        number += 1
   
    return primes[-1]

if __name__ == '__main__':
    n = int (input('Input sequence number of prime to find (E.g. 10001): ') )
    
    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(nthPrime( n ) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )