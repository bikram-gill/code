'''
File: kakuro.py

Code for generating number lists for solving Kakuro puzzle.
Kakuro involves filling out numbers 1-9 in each row/column, without repetitions, to add up to required number in the 2D grid.
It is like a crossword puzzle for simple addition, using just 9 letters (1-9)
'''
from itertools import combinations
from textwrap import TextWrapper

print("Praise God")

'''
kakuroNumberList function generates possible combinations of numbers which can add up to a specific number. 
Maximum number to which 1-9 numbers can add up to is 45.
'''
def kakuroNumberList():
    #digits available for generating sums, filling Kakuro grid
    numbers = [x for x in range(1,10)]
    d = dict()
    
    #find combinations for 2 or more numbers, mapped to each sum from 3 to 45
    for i in range(2,11):   
        for sublist in list(combinations(numbers,i)):
            s = sum(sublist)
            if s in d.keys():
                d[s].append(sublist)
            else:
                d[s] = [sublist]        
    
    return d

'''
simplePrintkakuroNumberList prints kakuroNumberList number return value, a dict, in simple format
'''
def simplePrintKakuroNumberList(d):
    print('::simplePrintkakuroNumberList:Start::')
    for k in d.keys():
        print(k, end=": ")
        print(d[k]) 
        print() 
    print('::simplePrintkakuroNumberList:End::')

'''
Simple main test function
'''
if __name__ == '__main__':
    simplePrintKakuroNumberList(kakuroNumberList())
    
