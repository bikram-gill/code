'''
Find Names scores of all the names in a file.
1. Sort the names
2. Find sum of alphabets in the name, A=1, B=2, etc
3. Multiple position * sum of alphabets
4. Total all the name scores

Input file name: P0022-Names.txt (should be placed in current working directory)
'''

from datetime import datetime
import string
import os

def namesScores(inputFile):
    
    file = open(inputFile, 'r')
    
    names = []
    
    line = file.readline().strip()

    names = line.replace("\"","").split(",")

    names.sort()
    
    s = 0

    for name, rank in zip(names, range(1,len(names)+1)):
        s += rank * sum(map(lambda x : string.ascii_uppercase.index(x) + 1, list(name)))
       
    return s
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(namesScores(os.curdir + '\code\solutions\projectEuler\python\P0022-Names.txt') ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )