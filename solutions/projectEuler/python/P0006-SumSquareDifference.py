'''
Find the difference between the sum of the squares of the natural numbers between min-max and the square of the sum.
'''

from datetime import datetime

def sumSquareDifference(min, max):
    
    sumNM = sum(range(min, max+1))
    
    squareOfSumNM = sumNM ** 2

    sumOfSquares = sum(list(map(lambda x : x * x, range(min, max+1))))

    return abs(squareOfSumNM - sumOfSquares)

if __name__ == '__main__':
    min, max = map( int, input('Input min and max (both inclusive), for finding sum square difference (E.g. 1 100): ').split() )
    
    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(sumSquareDifference( min, max ) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )