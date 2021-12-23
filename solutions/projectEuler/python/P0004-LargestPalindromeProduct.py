'''
Find largest palindromic number which is made up of product of n numbers, each made up of m digits.

NOTE: currently only n=2 is supported. For m > 3 memory error can occur in 32 bit version.
'''

from itertools import combinations_with_replacement, product
from datetime import datetime

#Find lowest and highest number made up of m digits
def findLowestAndHighest(m):
    numbers = []

    numbers.append(int('1'+'0'*(m-1)))    #1 followed by m-1 0s is the lowest m digit number
    numbers.append(int('9'*m))          #9 repeated m times is the highest m digit number

    return numbers

#Find all possible combinations of numbers from 100x-99x, calculate their product and check
def largestPalindrome(m, n):
    lowest, highest = findLowestAndHighest(m)

    largest_palindrome = 0

    for tup in list(combinations_with_replacement( range(lowest, highest+1), n)):
        prod = tup[0] * tup[1]
        str_prod = str(prod)
        
        if str_prod == str_prod[::-1]:
            if largest_palindrome < prod:
                largest_palindrome = prod

    return largest_palindrome


if __name__ == '__main__':
    digits = int( input('For largest palindromic number, enter number of digits (e.g. 3): ') )
    
    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(largestPalindrome( digits, 2 ) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )