'''
Find smallest number which is evenly divisible by all numbers from n, n+1, n+2... to m.

NOTE: Testing for arbitrary min and max is pending. 
'''

from datetime import datetime

#Find smallest number which is evenly divisible by all numbers from n, n+1, ... to m
def findSmallestMultiple(min, max):

    multiple = 1
    for i in range(min, max + 1):

        #if multiple not divisible by i, then find smallest multiple which 
        # will be divisible by i 
        if multiple % i != 0:
            for j in range(1, i+1):
                temp = multiple
                temp *= j
                if temp % i == 0:
                    multiple = temp
                    break
        
    return multiple

if __name__ == '__main__':
    min, max = map( int, input('Input min and max (both inclusive), for finding smallest multiple (E.g. 1 10): ').split() )
    
    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(findSmallestMultiple( min, max ) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )