'''
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
Note: takes approx 20 minutes.
'''

from datetime import datetime
from itertools import permutations
import os
import math

def nonAbundantSums():
    
    limit = 28124
    #find all abundant numbers
    abundantNumbers = []
    for i in range(1,limit+1):
        divisors = []
        for j in range(1,math.ceil(i/2)+1):
            if i % j == 0:
                divisors.append(j)
        
        if sum(divisors) > i:
            abundantNumbers.append(i)
    
    l = len(abundantNumbers)
    s = 0
    print(l)
    for i in range(1, limit+1):
        found = False
        for j in range(l):
            
            if found == True or abundantNumbers[j] > i:
                break

            for k in range(j, l):    
                a = abundantNumbers[j] + abundantNumbers[k]
                if(a > i):
                    break
                if(a == i):
                    found = True
                    break
        
        if found == False:
            s += i

    return s
    
if __name__ == '__main__':
    
    print(os.getcwd())

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(nonAbundantSums() ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )