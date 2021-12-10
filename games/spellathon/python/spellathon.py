'''
Code for generating word lists for solving Spellathon puzzle.
-Spellathon involves listing all possible words from 7 given alphabets. 
-One alphabet should exist in each word (the alphabet in the center, Z, in following example).
-Minimum word length is four letters.
-If a letter repeats in the alphabet list, the letter can repeat same number of times in the word.

-----B------
-A-------C--
-----Z------
-F-------D--
-----E------

Code in this file helps in generating and solving Spellathon puzzles

TO DO: exception and error handling
'''

import os

'''
parseWordListAndSaveLongWords - following function parses word list file, and generates a new file containing words of length 4 or more. Spellathon only needs words with length more than 3 (4 or more).
file parsed is './../data/words.txt' and file generated is './../data/long_words.txt'
'''
def parseWordListAndSaveLongWords(file_name_with_path):
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

'''
findWordsWithAlphabetsSimpleSearch takes a string with 7 letters with which words need to be created.

This function implements a simple logic, and other version will try to implement an optimized solution and/or use regex.

Assumptions:
-First alphabet in the string is the central letter, which needs to occur in each word.
-This function assumes that a file exists, ./../data/long_words.txt, which contains only words with length >= 4.
-Code assumes a temp folder exists in path './../data/temp', and it is used for storing temporary files
-This version assumes all chars are unique, and future version will handle duplicate chars.
-Lewand list of alphabets for most common to least common alphabets in appearance is used, to shortlist the word list faster: etaoinshrdlcumwfgypbvkjxqz
( https://en.wikipedia.org/wiki/Letter_frequency#Relative_frequencies_of_letters_in_the_English_language )
'''
def findWordsWithAlphabetsSimpleSearch(alphabetList):
    
    temp_file_names = ['temp_file'+str(x) for x in range(7)] #initialize temp file names
    
    parseWordListAndSaveWords('./../data/long_words.txt', temp_file_names[0], alphabetList[0])
    
    sorted_alphabets = sortSearchLettersAsPerFrequency(alphabetList[1:])
    
    previous_temp_file = temp_file_names[0]
    
    for char_to_search, temp_file in zip(sorted_alphabets, temp_file_names[1:]):
        parseWordListAndSaveWords('./../data/temp/' + previous_temp_file, temp_file, char_to_search)
        previous_temp_file = temp_file
    
    #Read final file
    final_word_file = open('./../data/temp/' + temp_file_names[-1], 'r')
    
    final_words = []
    final_word_count = 0
    
    while True:
        line = final_word_file.readline()
        
        if not line:
            break
        final_word_count += 1
        final_line = line.strip()
        final_words.append(final_line)
    
    final_word_file.close()
    
    print("Words with: {}, Count: {}".format( alphabetList, final_word_count))
    
    print(final_words)
    
    #TO DO: delete temp files
    
    return final_words
     
    
'''
parseWordListAndSaveWords - checks each word in input file for occurrence of a word, and saves these words in a new file.
'''
def parseWordListAndSaveWords(file_name_with_path, temp_file_name, char_to_search):
    words = open(file_name_with_path, 'r')
    
    char_words = open('./../data/temp/' + temp_file_name, 'w')
        
    readLines = 0
    writtenLines = 0
    
    while True:
        line = words.readline()
        
        if not line:
            break
        readLines += 1
        final_line = line.strip()
        if char_to_search in final_line:
            char_words.writelines( final_line + '\n')
            writtenLines += 1
    
    print("Char: {}, Lines read: {}, Lines written: {}".format( char_to_search, readLines, writtenLines))
    
    words.close()
    char_words.close()

    
'''
Sorts list in reverse order, based on occurrence in Lewand's alphabets (alphabet frequency).
This helps in short-listing the words faster
'''
def sortSearchLettersAsPerFrequency(alphabetList):
    lewandAlphabets = 'etaoinshrdlcumwfgypbvkjxqz'
    returnList = sorted(list(alphabetList), key = lambda x: lewandAlphabets.index(x))
    return returnList[::-1]

if __name__ == '__main__':
    parseWordListAndSaveLongWords('./../data/words.txt')
    findWordsWithAlphabetsSimpleSearch('petouzv')
    print('end')
    