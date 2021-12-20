import os

def sumMultiples(max, n):
    multiple = (max - 1) // n
    return n * multiple * (multiple + 1) / 2

def sumOfMultiplesOfNOrM(max, n, m):
    return sumMultiples(max, n) + sumMultiples(max, m) - sumMultiples(max, m*n)

if __name__ == '__main__':
    inputlist = list( map( int, input('Input upper bound, and 2 space separated numbers (e.g. 1000 3 5): ').split() ) )
    
    print('Answer: ' + str(sumOfMultiplesOfNOrM( inputlist[0], inputlist[1], inputlist[2] ) ) )