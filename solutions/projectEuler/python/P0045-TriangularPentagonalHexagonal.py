'''
Find nth (e.g. 2nd number) which satisfies following condition:
Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
'''

from datetime import datetime

def triangularPentagonalHexagonal(number):
    
    limit = 100000

    pentagons = []
    for n in range(1,limit+1):
        pentagons.append(n * ((3 * n ) - 1) / 2)

    triangles = []
    for n in range(1,limit+1):
        triangles.append(n * (1+ n ) / 2)

    hexagonals = []
    for n in range(1,limit+1):
        hexagonals.append(n * ((2 * n) - 1) )

    seq = 0

    for i in range(limit):
        if pentagons[i] in triangles:
            if pentagons[i] in hexagonals:
                print(pentagons[i])
                seq += 1
                if seq == number:
                    return pentagons[i]

    return 0
    
if __name__ == '__main__':

    number = int(input('What is the sequence of number to find (E.g. 3): '))

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(triangularPentagonalHexagonal(number) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )