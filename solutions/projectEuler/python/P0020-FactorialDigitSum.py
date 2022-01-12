'''
Sum of digits of n! (n factorial).
'''
from datetime import datetime

def sumOfDigitsOfFactorial(N):
    factorialArray = [0 for x in range(N+1)]

    factorialArray[1] = 1

    for i in range(2, N+1):
        factorialArray[i] = factorialArray[i-1] * i

    return sum(map(int, list(str(factorialArray[N]))))

if __name__ == '__main__':
    N = int( input('Input number (E.g. 100): ') )

    start = datetime.now()

    print('Answer: ', str( sumOfDigitsOfFactorial(N) ) )

    end = datetime.now()

    print( 'Start and end time: ', start.strftime("%H:%M:%S"), ' ', end.strftime("%H:%M:%S") )

    print( 'Time taken (s): ', round( (end - start).total_seconds() , 2) )
    print( 'Time taken (m): ', round( (end - start).total_seconds() / 60 , 2) )