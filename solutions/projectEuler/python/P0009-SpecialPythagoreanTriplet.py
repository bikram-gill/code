'''
Find a*b*c, where a+b+c = N, and a square + b square = c square, and a < b < c.
'''

from datetime import datetime
import math
import itertools


def specialPythagoreanTriplet(N):

    for a, b in itertools.product(range(1,N+1), range(1,N+1)):
        c = N - a - b
        if a < b and b < c:
            if (a**2) + (b**2) == (c**2):
                #print(a,b,c)
                return a*b*c

if __name__ == '__main__':
    N = int (input('Input a+b+c (E.g. 1000): ') )
    
    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(specialPythagoreanTriplet( N) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )