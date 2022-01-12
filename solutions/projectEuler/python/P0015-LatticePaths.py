'''
Number of paths (between 2 diagonal corners) along edges of a NxN grid, 
only moving right or down = (2 * N)! / (N! * N!)
'''
from datetime import datetime

def factorial(N):
    factorialArray = [0 for x in range(N+1)]

    factorialArray[1] = 1

    for i in range(2, N+1):
        factorialArray[i] = factorialArray[i-1] * i

    return factorialArray[N]

def numberOfLatticePaths(N):
    
    Numerator = factorial(2 * N)
    Denominator = factorial (N)

    return int(Numerator / (Denominator * Denominator))

if __name__ == '__main__':
    N = int( input('Input number of edges (E.g. 20): ') )

    start = datetime.now()

    print('Answer: ', str( numberOfLatticePaths(N) ) )

    end = datetime.now()

    print( 'Start and end time: ', start.strftime("%H:%M:%S"), ' ', end.strftime("%H:%M:%S") )

    print( 'Time taken (s): ', round( (end - start).total_seconds() , 2) )
    print( 'Time taken (m): ', round( (end - start).total_seconds() / 60 , 2) )