'''
Find sum of all numbers, where sum of each digit raised to power n is equal to the number.
'''

from datetime import datetime
import os

def digitFifthPowers( power):

    s = 0

    #try all numbers from 10 to 1M
    for n in range(10, 1000001):
        sum_of_digits = 0
        for digit in list(str(n)):
            sum_of_digits += pow(int(digit), power)
        
        if(sum_of_digits == n):
            s += n

    return s
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    power = int( input('Input the power to use (E.g. 5): ') )

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(digitFifthPowers( power) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )