'''
Code for generating word lists for solving Spellathon puzzle.
-Spellathon involves listing all possible words from 7 given alphabets. 
-One alphabet should exist in each word (the alphabet in the center, Z, in following example).
-Minimum word length is four letters.

-----B------
-A-------C--
-----Z------
-F-------D--
-----E------

Code in this file helps in generating and solving Spellathon puzzles
'''

import os

'''
parseWordListAndSaveLongWords - following function parses word list file, and generates a new file containing words of length 4 or more. Spellathon only needs words with length more than 3 (4 or more).
file parsed is './../words.txt' and file generated is './../long_words.txt'
'''
def parseWordListAndSaveLongWords(file_name_with_path):
    print(os.curdir)
    words = open(file_name_with_path, 'r')
    
    long_words = open('./../data/long_words.txt', 'w')
        
    readLines = 0
    writtenLines = 0
    
    while True:
        line = words.readline()
        
        if not line:
            break
        readLines += 1
        final_line = line.strip()
        if len(final_line) > 3:
            long_words.writelines( final_line + '\n')
            writtenLines += 1
    
    print("Lines read: {}, Lines written: {}".format( readLines, writtenLines))
    
    words.close()
    long_words.close()

if __name__ == '__main__':
    #parseWordListAndSaveLongWords('./../data/words1.txt')
    parseWordListAndSaveLongWords('./../data/words.txt')
    pass