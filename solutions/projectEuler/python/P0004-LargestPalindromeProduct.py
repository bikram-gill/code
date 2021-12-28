'''
Find largest palindromic number which is made up of product of n numbers, each made up of m digits.

NOTE: currently only n=2 is supported. In largestPalindrome (combinations_with_replacement), for 
m > 3 memory error can occur in 32 bit python. For m > 4 memory error will occur in 64 bit python.
Version2 supports larger digit numbers (but could take few minutes to execute for m > 6).
'''

from itertools import combinations_with_replacement
from datetime import datetime

#Find lowest and highest number made up of m digits
def findLowestAndHighest(m):
    numbers = []

    numbers.append(int('1'+'0'*(m-1)))    #1 followed by m-1 0s is the lowest m digit number
    numbers.append(int('9'*m))          #9 repeated m times is the highest m digit number

    return numbers

#Find all possible combinations of numbers from 100x-99x, calculate their product and check.
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

#Find all possible combinations of numbers from 100x-99x, calculate their product and check.
#Without itertools for large numbers.
def largestPalindromeV2(m, n):
    lowest, highest = findLowestAndHighest(m)

    largest_palindrome = 0

    for i in range(highest, lowest - 1, -1):

        #if palindrome is already larger than largest possible product, then terminate
        #as further products would be lesser
        if largest_palindrome > (i * highest):
            break

        for j in range(highest, lowest - 1, -1):

            prod = i * j

            #if palindrome is already larger than the prod, terminate inner loop
            #as further products would be lesser
            if largest_palindrome > prod:
                break

            str_prod = str(prod)
            
            if str_prod == str_prod[::-1]:
                if largest_palindrome < prod:
                    largest_palindrome = prod

    return largest_palindrome


if __name__ == '__main__':
    digits = int( input('For largest palindromic number, enter number of digits (e.g. 3): ') )
    
    start = datetime.now().strftime("%H:%M:%S")

    #if digits cannot be handled by 32 bit system, don't use itertools 
    if digits > 3:
        print('Answer (V2): ', str(largestPalindromeV2( digits, 2 ) ) )
    else:
        print('Answer: ', str(largestPalindrome( digits, 2 ) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )