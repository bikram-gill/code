'''
Find first N digits of sum of M L-digit numbers.

Input numbers are read from a file containing one number in each line. 
Input file name: P0013-LargeSum-Input.txt (should be placed in current working directory)
'''

from datetime import datetime
import os

def firstNDigitsOfSum(N, inputFile):
    
    file = open(inputFile, 'r')
    
    sum = 0
    
    while True:
        line = file.readline().strip()
        
        if not line:
            break

        print(sum, ' ', line)
        sum += int(line)

    print(sum)

    return str(sum)[0:N]
    
if __name__ == '__main__':
    print(os.getcwd())
    N = int (input('Number of leading digits to read (E.g. 10): ') )

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(firstNDigitsOfSum(N, os.curdir + '\solutions\projectEuler\python\P0013-LargeSum-Input.txt') ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )