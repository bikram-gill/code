'''
Find sum of all amicable number less than N.
'''

from datetime import datetime

#This method can take upto 30+ seconds for N > 30000
def sumOfAmicableNumbers(N):
      
    amicableNumbers = set()

    for number in range(1,N+1):
        
        sumDivisors1 = sum([x for x in range(1, (number // 2) + 1) if number % x == 0])
        sumDivisors2 = sum([x for x in range(1, (sumDivisors1 // 2) + 1) if sumDivisors1 % x == 0])
        
        if sumDivisors2 == number and  sumDivisors1 != number:
            amicableNumbers.add(number)
            amicableNumbers.add(sumDivisors1)
      
    return sum(amicableNumbers)

#A faster version and can process N == 1M in less than 10 seconds
def sumOfAmicableNumbersFast(N):

    #random number found by testing, for N == 1M, times should be atleast 4
    times = 4

     #1 is a divisor for all integers
     #Initialize 2D array to store divisors of number at respective indexes  
    divisors = [ [1] for i in range(times*N+1)]

    for number in range(2,times*N+1):
        for multiple in range(number*2, N+1, number):
            divisors[multiple].append( number )

    #Dictionary to store sum of divisors for each number
    sumOfDivisors = dict()
    for number in range(1,times*N+1):
        sumOfDivisors[number] = sum(divisors[number])

    amicableNumbers = set()

    for number in sumOfDivisors:

        if number > N:
            break

        sumOfDivisor = sumOfDivisors[number]
        
        if number == sumOfDivisors[sumOfDivisor] and sumOfDivisor != number:
            amicableNumbers.add(number)
            amicableNumbers.add(sumOfDivisor)

    return sum(amicableNumbers)

if __name__ == '__main__':
    N = int( input('Input upper bound for finding sum of amicable numbers (E.g. 10000): ') )

    start = datetime.now()

    #print('Answer: ', str( sumOfAmicableNumbers(N) ) )
    print('Answer: ', str( sumOfAmicableNumbersFast(N) ) )

    end = datetime.now()

    print( 'Start and end time: ', start.strftime("%H:%M:%S"), ' ', end.strftime("%H:%M:%S") )

    print( 'Time taken (s): ', round( (end - start).total_seconds() , 2) )
    print( 'Time taken (m): ', round( (end - start).total_seconds() / 60 , 2) )