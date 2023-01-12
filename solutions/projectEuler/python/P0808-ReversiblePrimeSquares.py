'''
Find sum of first n reversible prime squares.
Reversible prime square is square of a prime, not a palindrome, and its reverse is also square of prime.
'''

from datetime import datetime
import os

def reversiblePrimeSquare(limit):
    
    nums = 50000000
    
    primes = [1] * nums
    primes[0] = 0
    primes[1] = 0
    for i in range(2, nums):
        for j in range(2 * i, nums, i):
            primes[j] = 0

    primeSquares = []
    primesSquaresSet = set()
    for i in range(2, nums):
        if primes[i] == 1:
            ii = i*i
            primeSquares.append(ii)
            primesSquaresSet.add(ii)

    s = 0
    count = 0
    for i in primeSquares:
        si = str(i)
        rsi = si[::-1]
        ri = int(rsi)
        if ri in primesSquaresSet and si != rsi:
            count += 1
            print(count, i)
            s += i
            if count == limit:
                return s

    return 0


if __name__ == '__main__':
    
    print(os.getcwd())
    
    limit = int(input('How many reversible prime squares to sum (E.g. 50): '))

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(reversiblePrimeSquare(limit) ) )
    
    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )