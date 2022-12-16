'''
What is the largest 1 to 9 (limit) pandigital 9(limit)-digit number that can be formed as the concatenated 
product of an integer with (1,2, ... , n) where n > 1?
'''

from datetime import datetime
import os

def panditigalMultiples(limit):
    pandigital = '123456789'
    num = 0
    #number (range using random testing)
    for i in range(100000):
        #range
        for j in range(1,20):
            #calculate number
            s = ''
            for k in range(1,j):
                s += str(i*k)
            
            if(pandigital[0:limit] == ''.join(sorted(s))):
                print(s)
                if(num < int(s)):
                    num = int(s)

    return num
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    limit = int(input('What is the highest limit of the pandigital number to find, range 1-9 (E.g. 9): '))

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(panditigalMultiples(limit) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )