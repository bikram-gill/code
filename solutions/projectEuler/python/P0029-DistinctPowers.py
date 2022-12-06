'''
Find number of distinct powers a^b, where a and b are in range min, max (inclusive).
'''

from datetime import datetime
import os

def distinctPowers(min, max):

    r = set()

    for a in range(min, max+1):
        for b in range(min, max+1):
            r.add( pow(a,b) )

    return len(r)
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    min, max = map (int, input('Input min and max numbers to consider (E.g. 2 100): ').split() )

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(distinctPowers( min, max) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )