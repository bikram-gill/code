'''
Count total number of alphabets in all word representation of numbers between 1 and 1000. Use British 
form of number with 'and', e.g. one hunderd and two.
'''
import os
from datetime import datetime
#pip install num2words (in some IDE this library is not being identified, so program can be executed from command prompt)
from num2words import num2words

def numberLetterCounts( min, max):

    count = 0

    for i in range(min, max+1):
        s = num2words(i)
        count += len([a for a in list(s) if a.isalpha()])

    return count

if __name__ == '__main__':
     
    print(os.getcwd())
    
    min, max = list(map( int, input('Input start and end number (e.g. 1 1000): ').split() ) )

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str( numberLetterCounts( min, max) ) )
    
    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )