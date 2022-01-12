'''
For sum of digits of n ** m.
'''
from datetime import datetime
    
if __name__ == '__main__':
    n, m = map ( int, input('Input number and power (E.g. 2 1000): ').split() )

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str( sum(int(x) for x in str(n ** m)) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )