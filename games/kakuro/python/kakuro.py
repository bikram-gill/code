'''
Code for generating number lists for solving Kakuro puzzle.
Kakuro involves filling out numbers 1-9 in each row/column, without repetitions, to add up to required number in the 2D grid.
It is like a crossword puzzle for simple addition, using just 9 letters (1-9)
'''
from itertools import combinations
from itertools import permutations
from textwrap import TextWrapper

'''
kakuroNumberList function generates possible combinations of numbers which can add up to a specific number. 
Maximum number to which 1-9 numbers can add up to is 45.
'''
def kakuroNumberList():
    #digits available for generating sums, for filling Kakuro grid
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
simplePrintKakuroNumberList prints kakuroNumberList number return value, a dict, in simple name value format.
function input parameter is a dict variable, with a number mapped to a list of tuples, with each tuple having number combination adding up to the respective key.
'''
def simplePrintKakuroNumberList(d):
    print('::simplePrintkakuroNumberList:Start::')
    for k in d.keys():
        print(k, end=": ")
        print(d[k]) 
        print() 
    print('::simplePrintkakuroNumberList:End::')


'''
List of all the number words that can be used to solve kakuro - basically a permutation of all possible combinations.
E.g. 12, 21, 13, 31, etc
'''
def kakuroWordList():
    d = kakuroNumberList()
    
    dp = dict()
    
    for k in d.keys():
        dp[k] = []
        for tup in d[k]:
            dp[k].append( list(permutations(tup)) )
            #to do: join tuple to final word
        #print(dp[k]) 

    return dp


'''
simplePrintKakuroWordList prints kakuroNumberList number return value, a dict, in simple name value format.
function input parameter is a dict variable, with a number mapped to a list of tuples, with each tuple having number combination adding up to the respective key.
'''
def simplePrintKakuroWordList(d):
    print('::simplePrintKakuroWordList:Start::')
    for k in d.keys():
        print(k, end=": ")
        print(d[k]) 
        print() 
    print('::simplePrintKakuroWordList:End::')

'''
Simple main test function
'''
if __name__ == '__main__':
    #simplePrintKakuroNumberList(kakuroNumberList()) #uncomment for simple 
    #tablePrintKakuroNumberList(kakuroNumberList())
    simplePrintKakuroWordList(kakuroWordList())
