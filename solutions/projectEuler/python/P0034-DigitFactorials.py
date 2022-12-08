'''
Find sum of all numbers which are equal to sum of factorials of its digits.
'''

from datetime import datetime
import os

def digitFactorials():

    factorials = []
    for i in range(0, 10):
        if(i == 0):
            factorials.append(1)
        else:
            factorials.append(factorials[i-1]*i)

    #try for a million numbers
    total = 0
    for j in range(10, 1000001):
        s = 0
        for d in list(str(j)):
            s += factorials[int(d)]
        
        if s == j:
            total += s
            print(s)

    return total
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(digitFactorials() ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )