'''
Find first number to violate Goldbach's conjecture
'''

from datetime import datetime

def goldbachsOtherConjecture(number):
    
    limit = 100000
    #generate list of twice of squares
    twiceSquares = []
    for i in range(limit):
        twiceSquares.append(2 * i * i)

    #generate list of primes
    primes = [1] * limit
    primes[0] = 0
    primes[1] = 0
    for i in range(2,limit):
        for j in range(i*2, limit, i):
            primes[j] = 0
    
    primeNumbers = []
    for i in range(limit):
        if primes[i] == 1:
            primeNumbers.append(i)

    #generate list of odd composites
    oddComposites = [0] * limit
    for i in range(3,limit, 2):
        for j in range(i*2, limit, i):
            oddComposites[j] = 1
    #clear out even composites
    for i in range(2,limit, 2):
        oddComposites[i] = 0

    oddCompositeNumbers = []
    for i in range(limit):
        if oddComposites[i] == 1:
            oddCompositeNumbers.append(i)

    #print('twice squares', twiceSquares)
    #print('primes', primeNumbers)
    #3print('odd composites', oddCompositeNumbers)
    
    #test the conjecture
    num = 0
    for a in oddCompositeNumbers:
        found = False
        for b in primeNumbers:
            if b > a:
                break
            for c in twiceSquares:
                if (b + c ) == a:
                    #print(b, c, '=', a)
                    found = True
                    break
                if b + c > a:
                    break
        
        if not found:
            num += 1
            print('found', num, a)
            if num == number:
                return a

    return 0
    
if __name__ == '__main__':

    number = int(input('What is the sequence of number to find (E.g. 1): '))

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(goldbachsOtherConjecture(number) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )