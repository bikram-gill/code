'''
Find a number whose square is of form 1-2-3-4-5-6-7-8-9-0. Where - is a digit.
'''

from datetime import datetime
import os
import math
import re

def concealedSquare():
    min = math.floor(math.sqrt(1020304050607080900))
    max = 1389026620 #math.ceil(math.sqrt(1929394959697989990))

    #going from min to max can taken a long time, reverse search goes much faster
    for i in range(max,min,-10):
        a = i * i
        s = str(a)
        if re.fullmatch(r'^1.2.3.4.5.6.7.8.9.0$',s) != None:
            return i

    return 0

if __name__ == '__main__':
    
    print(os.getcwd())
    
    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(concealedSquare() ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )