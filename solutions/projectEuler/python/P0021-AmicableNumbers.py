'''
Find sum of all amicable number less than N.
'''

from datetime import datetime

def sumOfAmicableNumbers(N):
      
    amicableNumbers = set()

    for number in range(1,N+1):
        
        sumDivisors1 = sum([x for x in range(1, (number // 2) + 1) if number % x == 0])
        sumDivisors2 = sum([x for x in range(1, (sumDivisors1 // 2) + 1) if sumDivisors1 % x == 0])
        
        if sumDivisors2 == number and  sumDivisors1 != number:
            amicableNumbers.add(number)
            amicableNumbers.add(sumDivisors1)
      
    return sum(amicableNumbers)

if __name__ == '__main__':
    N = int( input('Input upper bound for finding sum of amicable numbers (E.g. 10000): ') )

    start = datetime.now()

    print('Answer: ', str( sumOfAmicableNumbers(N) ) )

    end = datetime.now()

    print( 'Start and end time: ', start.strftime("%H:%M:%S"), ' ', end.strftime("%H:%M:%S") )

    print( 'Time taken (s): ', round( (end - start).total_seconds() , 2) )
    print( 'Time taken (m): ', round( (end - start).total_seconds() / 60 , 2) )