'''
Find last m digits of 1 ** 1 + 2 ** 2 + ... + n ** n
'''

from datetime import datetime

def selfPowers(N, digits):
    
    sum = 0

    for i in range(1, N+1):
        sum += i ** i

    strSum = str(sum)

    return strSum[-digits:]
    
if __name__ == '__main__':
    N, m = map(int, input('N for self power and number of digits (E.g. 1000 10): ').split() )

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(selfPowers(N,m) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )