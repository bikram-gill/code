'''
Find sum of all fibonacci numbers upto Max, which are also divisible by n.
'''

def sumOfEvenFibonacci( max, divisor):
    first = 1
    second = 2
    next_number = 0
    sum_fib = second

    while next_number <= max:
        next_number = first + second
        sum_fib += next_number if next_number % divisor == 0 else 0

        first = second
        second = next_number

    return sum_fib

if __name__ == '__main__':
    max, divisor = list(map( int, input('Input upper bound and divisor (e.g. 4000000 2): ').split() ) )
    
    print('Answer: ', str(sumOfEvenFibonacci( max, divisor ) ) )