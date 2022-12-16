'''
'''

from datetime import datetime
import os

def champernownesConstant():
    s = ''
    for i in range(1,1000000):
        s += str(i)
    
        print(len(s))
    
        if(len(s) > 1000000):
            print(i)
            break

    return (int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999]) )

    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(champernownesConstant() ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )