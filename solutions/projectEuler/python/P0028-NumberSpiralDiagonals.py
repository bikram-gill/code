'''
Sum of numbers in diagonals for spiral of side n (1001):
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
'''

from datetime import datetime
import os

def numberSpiralDiagonals(limit):

    sum = 1
    num = 1
    step = 0

    while ((step+1) < limit):
        step += 2
        numInSquare = 4
        while (numInSquare > 0):
            num += step
            sum += num
            numInSquare -= 1
        
        print(step+1, sum)

    return sum
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    limit = int(input('Input max length of spiral (E.g. 1001): '))

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(numberSpiralDiagonals( limit) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )