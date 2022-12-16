'''
For which right-angle triangle perimeter < limit, is number of integer combinations maximum. 
'''

from datetime import datetime
import os

def integerRightTriangles(limit):
    #a+b+c = limit
    #a^2 + b^2 = c^2

    d = dict()

    for a in range(1,limit):
        a2 = a * a
        
        for b in range(1,limit):
            b2 = b * b
            
            for c in range(1, limit - a - b):
                lim = a + b + c

                if((c*c) == (a2+b2)):
                    if lim in d:
                        d[lim] += 1
                    else:
                        d[lim] = 1
                    
                    print(lim, a, b, c)

    print(d)

    return max(d,key=d.get)
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    limit = int(input('What is the highest perimeter limit (E.g. 1000): '))

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(integerRightTriangles(limit) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )