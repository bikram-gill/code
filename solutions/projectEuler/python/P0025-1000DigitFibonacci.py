'''
Find first fibonacci number with n digits - find its index (sequence in the series).
'''

from datetime import datetime
import os

def nDigitFibonacci(digits):
    
    f1 = 1;
    f2 = 1;
    index = 2

    notFound = True

    while notFound:
        f3 = f1 + f2
        index += 1

        if len(str(f3)) == digits:
            notFound = False

        f1 = f2
        f2 = f3


    return index
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    digits = int( input('Enter number to digits (e.g. 1000): ') )

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(nDigitFibonacci( digits) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )