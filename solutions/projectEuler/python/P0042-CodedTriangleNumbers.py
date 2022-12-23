'''
Find total number of triangle words in a input file.
Input file name: P0042-words.txt (should be placed in current working directory)
'''

from datetime import datetime
import string
import os

def namesScores(inputFile):
    
    file = open(inputFile, 'r')
    
    names = []
    line = file.readline().strip()
    names = line.replace("\"","").split(",")
    
    maxTN = (string.ascii_uppercase.index('Z')+1) * max([len(name) for name in names])
    print('Max triangle number value to consider: ', maxTN)

    numbers = [] #triangular numbers
    for i in range(1000000):
        num = 0.5 * i * (i+1)
        if num > maxTN:
            break
        numbers.append(num)

    count = 0
    for name in names:
        wordNum = sum([(string.ascii_uppercase.index(x) + 1) for x in list(name)])
        if wordNum in numbers:
            count += 1

    return count

if __name__ == '__main__':
    
    print(os.getcwd())
    
    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(namesScores(os.curdir + '\code\solutions\projectEuler\python\P0042-words.txt') ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )