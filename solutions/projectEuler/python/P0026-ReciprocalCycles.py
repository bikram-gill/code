'''
From 1/2 to 1/n, which fraction contains largest recurring cycle, find n
'''

from datetime import datetime
import os

def numberSpiralDiagonals(limit):

    largestRepeatingNumber = 0

    largestRecCycle = 0

    for i in range(2, limit):
        j = 10
        remainders = []
        repeatingRemainder = 0
        while (True):
            if j < i:
                j = j * 10
                continue
            else:
                j = j % i
                if j == 0:
                    break
                if j in remainders:
                    repeatingRemainder = j
                    break
                remainders.append(j)

        recLen = 0        
        if repeatingRemainder != 0:
            recLen = len(remainders) - remainders.index(repeatingRemainder)

        if recLen > largestRecCycle:
            largestRecCycle = recLen
            largestRepeatingNumber = i

        print(i, recLen)
        
    return largestRepeatingNumber
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    limit = int(input('Input max limit to find the longest recurring cycle (E.g. 1000): '))

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(numberSpiralDiagonals( limit) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )