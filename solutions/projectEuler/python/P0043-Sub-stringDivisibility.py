'''
Find all 0-9 pandigital numbers where some sub-strings are divisible by specific numbers
'''

from datetime import datetime
from itertools import permutations

def subStringDivisibility():
    
    digits = '0123456789'

    perms = [''.join(p) for p in permutations(digits)]

    s = 0

    for perm in perms:
        if int(perm[1:4])%2 == 0 and int(perm[2:5])%3 == 0 and int(perm[3:6])%5 == 0 and int(perm[4:7])%7 == 0 and int(perm[5:8])%11 == 0 and int(perm[6:9])%13 == 0 and int(perm[7:10])%17 == 0:
            print(perm)
            s += int(perm)

    return s
    
if __name__ == '__main__':

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(subStringDivisibility() ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )