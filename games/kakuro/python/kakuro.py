'''
Code for generating number lists for solving Kakuro puzzle.
Kakuro involves filling out numbers 1-9 in each row/column, without 
repetitions, to add up to required number in the 2D grid.
It is like a crossword puzzle for simple addition, using just 9 
letters (1-9)
'''
from itertools import combinations
from itertools import permutations

'''
kakuroNumberList function generates possible combinations of numbers
 which can add up to a specific number. 
 
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
simplePrintKakuroNumberList prints kakuroNumberList number return value,
 a dict, in simple name value format.
 
function input parameter is a dict variable, with a number mapped to a 
list of tuples, with each tuple having number combination adding up to 
the respective key.

input: dict d - the dictionary to print

'''
def simplePrintKakuroNumberList(d):
    print('::simplePrintkakuroNumberList:Start::')
    for k in d.keys():
        print(k, end=": ")
        print(d[k]) 
        print() 
    print('::simplePrintkakuroNumberList:End::')


'''
List of all the number words that can be used to solve kakuro - basically
 a permutation of all possible combinations.
E.g. 12, 21, 13, 31, etc
'''
def kakuroWordList():
    num_dict = kakuroNumberList()
    
    word_dict = dict()
    
    for k in num_dict.keys():
        word_dict[k] = []
        
        #transform the collection of list integers into corresponding string
        for tup in num_dict[k]:
            word_dict[k] = [''.join(map(str,tup2)) for tup2 in list(permutations(tup))]
        
    return word_dict


'''
simplePrintKakuroWordList prints kakuroNumberList number return value, 
a dict, in simple name value format.

function input parameter is a dict variable, with a number mapped to a 
list of tuples, with each tuple having number combination adding up to the respective key.

input: dict d - the dictionary to print
'''
def simplePrintKakuroWordList(d):
    print('::simplePrintKakuroWordList:Start::')
    for k in d.keys():
        #print key and word values
        #TODO fix "str: Too large to show contents. Max items to show: 
        #300" error for key 28 and above
        print(k, end=": ")
        for value in d[k]:
            print(value, end=" ")  
        print()  
    print('::simplePrintKakuroWordList:End::')

'''
simplePrintStatKakuro - prints simple statistics about kakuro numbers
'''
def simplePrintStatKakuro():
    print('::simplePrintStatKakuro:Start::')
    
    numbers = kakuroNumberList()
    total_numbers = sum([len(tup_list) for tup_list in numbers.values()])
        
    print('Number of possible sums: ', len(numbers.keys())) #43
    print('Minimum and maximum sum, with range: ', numbers.keys())
    print('Maximum number of letter combinations possible: ', total_numbers) #502
    print('Letter combinations per sum:')
    for key, value in numbers.items():
        print('sum: ', key, '    combinations: ', len(value) )

    
    words = kakuroWordList()
    total_words = sum([len(tup_list2) for tup_list2 in words.values()])
    print('Maximum number words possible (permutations): ', total_words) #771990
    print('Word combinations per sum:')
    #for key, value in words.items():
    #    print(key, ' ', len(value) )

    print('::simplePrintStatKakuro:End::')



'''
Simple main test function
'''
if __name__ == '__main__':
    #simplePrintKakuroNumberList(kakuroNumberList()) #uncomment for simple 
    #tablePrintKakuroNumberList(kakuroNumberList())
    #simplePrintKakuroWordList(kakuroWordList())
    simplePrintStatKakuro()
    

