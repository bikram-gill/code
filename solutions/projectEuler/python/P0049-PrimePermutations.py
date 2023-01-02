'''
Find 3 primes made up of same digits and equal difference between the 3.
'''

from datetime import datetime

def primePermutations():
    limit = 10000 #all primes till 9999
    primes = [1] * (limit+1)

    primes[0] = 0
    primes[1] = 0
    for i in range(2,limit):
        for j in range(2*i,limit,i):
            primes[j] = 0

    primeNumbers = [] #actual 4 digit primes
    for i in range(limit):
        if(primes[i] == 1 and len(str(i)) == 4):
            primeNumbers.append(i)
            print(i)

    ret = []
    for i in range(len(primeNumbers)):
        s1 = ''.join(sorted(list(str(primeNumbers[i]))))
        
        for j in range(i+1,len(primeNumbers)):
            s2 = ''.join(sorted(list(str(primeNumbers[j]))))

            if(s1 == s2):
                diff = primeNumbers[j] - primeNumbers[i]
                newNum = diff + primeNumbers[j]
                s3 =  ''.join(sorted(list((str(newNum)))))

                if(s3 == s1) and newNum in primeNumbers:
                    print(primeNumbers[i], primeNumbers[j], newNum)
                    ret.append(str(primeNumbers[i]) + str(primeNumbers[j]) + str(newNum))
    return ret
    
if __name__ == '__main__':

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(primePermutations() ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )