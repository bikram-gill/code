'''
Find 2 pentagonal numbers (Pn=n(3n−1)/2), such that sum and difference of 2 pentagonal numbers is also pentagonal;
while the difference between the 2 numbers is smallest. Find the difference.
note: takes about 20 minutes
'''

from datetime import datetime
from itertools import combinations

def pentagonNumbers():
    
    pentagons = []
    limit = 10000
    for n in range(1,limit+1):
        pentagons.append(n * ((3 * n ) - 1) / 2)

    diff = pentagons[limit-1]
    found = False

    for i in range(limit):
        for j in range(i+1, limit):
            if found and (pentagons[j]-pentagons[i]) > diff:
                continue

            if (pentagons[j] - pentagons[i]) in pentagons:
                print(pentagons[j], pentagons[i])

                if (pentagons[j] + pentagons[i]) in pentagons:
                    print('found:',pentagons[i], pentagons[j])
                    if diff > (pentagons[j]-pentagons[i]):
                        diff = (pentagons[j]-pentagons[i])
                        found = True

    return diff
    
if __name__ == '__main__':

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(pentagonNumbers() ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )