'''
Find sum of numbers, upto n, which are palindromes in base 10 and 2.
'''

from datetime import datetime
import os

def doublebasePalindromes(limit):

    s = 0

    for i in range(limit+1):
        stri = str(i)
        strib = bin(i)[2:]

        if stri == stri[::-1] and strib == strib[::-1]:
            s += i
            print(stri, strib)

    return s
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    limit = int(input('What is the highest limit to find sum of palindromes (E.g. 1000000): '))

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(doublebasePalindromes(limit) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )