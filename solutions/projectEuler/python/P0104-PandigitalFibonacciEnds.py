'''
Find the nth fibonacci number, which is pandigital 1-n at both ends 
'''

from datetime import datetime
import os

#Brute force method, takes a couple of hours to execute
def integerRightTriangles1(limit):

    f1 = 1
    f2 = 1
    f3 = 0
    fn = 2

    pandigital = '123456789'

    for i in range(10000000):
        fn += 1
        f3 = f1 + f2

        print(fn)
        
        #check pandigital
        fstr = str(f3)
        if len(fstr) < 9:
            f1 = f2
            f2 = f3
            continue

        first = fstr[:9]
        last = fstr[-9:]

        if ''.join(sorted(first)) == pandigital:
            if ''.join(sorted(last)) == pandigital:
                print(f3)
                return fn

        f1 = f2
        f2 = f3

    return 0

#For better performance
def integerRightTriangles2(limit):
    return

if __name__ == '__main__':
    
    print(os.getcwd())
    
    limit = int(input('What is the highest limit for pandigital ends (E.g. 9): '))

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(integerRightTriangles1(limit) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )