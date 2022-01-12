'''
For all numbers below N, find the number with longest collatz sequence.
'''

from datetime import datetime

def collatzSequence(N):

    #store pre-calculated values of sequence, so it does not need to be recalculated for 
    # each number
    calculatedLengths = dict()
    
    calculatedLengths[1] = 1

    maxLengthNumber = 1

    for number in range(2, N+1):

        #starting count with the number itself
        calculatedLength = 1

        i = number

        while True:
            if i == 1:
                calculatedLength += 1
                break
            elif i in calculatedLengths:
                calculatedLength += calculatedLengths[i]
                break
            elif i % 2 == 0:
                calculatedLength += 1
                i = i / 2
            elif i % 2 != 0:
                calculatedLength += 1
                i = (3 * i) + 1
        
        calculatedLengths[number] = calculatedLength

        if calculatedLengths[maxLengthNumber] < calculatedLength:
            maxLengthNumber = number

    return maxLengthNumber
    
if __name__ == '__main__':
    N = int ( input('N for upper bound, to find longest collatz sequence (E.g. 1000000): ') )

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(collatzSequence(N) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )