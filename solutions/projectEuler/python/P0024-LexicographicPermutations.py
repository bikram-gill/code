'''
Find nth lexographic permutation of given input digits.
'''

from datetime import datetime
from itertools import permutations
import os

def lexicographicPermutations(digits, num):
    
    permutationList = permutations(digits)
    
    finalList = []
    
    for perm in list(permutationList):
        finalList.append(''.join(perm))

    finalList.sort()

    return finalList[num-1]
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    digits = input('Enter digits for permutation (e.g. 0123456789): ')
    num = int( input('Enter number to find (e.g. 1000000): ') )

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(lexicographicPermutations( digits, num) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )