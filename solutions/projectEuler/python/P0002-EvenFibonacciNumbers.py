import os


def sumOfEvenFibonacci( upper_limit ):
    first = 1
    second = 2
    next_number = 0
    sum_fib = second

    while next_number <= upper_limit:
        next_number = first + second
        sum_fib += next_number if next_number % 2 == 0 else 0

        first = second
        second = next_number

    return sum_fib

if __name__ == '__main__':
    n = int( input('Input upper bound (e.g. 4000000): ') )
    
    print('Answer: ', str(sumOfEvenFibonacci( n ) ) )