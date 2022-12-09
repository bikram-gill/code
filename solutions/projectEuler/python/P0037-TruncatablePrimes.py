'''
Find sum of all 11 primes, which are truncatable from left and right, and always yield primes.
'''

from datetime import datetime
import os

def truncatablePrimes(limit):

    isPrime = [1] * (limit+1)
    isPrime[0] = 0
    isPrime[1] = 0

    #prepare prime array
    for i in range(2,limit+1):
        for j in range(i*2, limit+1, i):
            isPrime[j] = 0
    
    s = 0
    for k in range(11, limit+1):
        st = str(k)
        isTruncatable = True
        #truncate from left
        for x in range(len(st)):
            if isPrime[int(st[x:])] == 0:
                isTruncatable = False
                break

        #truncate from right
        for x in range(-1, -len(st), -1):
            if isPrime[int(st[:x])] == 0:
                isTruncatable = False
                break
            
        if isTruncatable:
            print(k)
            s += k

    return s
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    limit = int(input('What is the highest limit to find sum of truncatable primes (E.g. 1000000): '))

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(truncatablePrimes(limit) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )