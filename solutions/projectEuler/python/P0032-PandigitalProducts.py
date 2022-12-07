'''
Find sum of all x, such that combinations m * n = x, where m, n, and x together are pandigital 1-9.
'''

from datetime import datetime
import os

def pandigitalProducts(digits):

    s = set()
    panDigits = ''.join(sorted(digits))
    panDigitsLen = len(digits)

    #try all numbers from 1 to 1M
    for m in range(1, 1000001):
        for n in range(1, 1000001):
            x = m * n

            y = str(x) + str(m) + str (n)

            if len(y) > panDigitsLen:
                break

            if len(y) == panDigitsLen and ''.join(sorted(y)) == panDigits:
                s.add(x)
                print('number',x,m,n)
        
        #break if digits more than panDigitsLen
        x = m * 2
        y = str(x) + str(m) + str (n)
        if len(y) > panDigitsLen:
            break
    
    print(s)

    return sum(list(s))
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    digits = input('Input pandigital digits to compare (E.g. 123456789): ')

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(pandigitalProducts(digits) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )