'''
Code for generating word lists for solving Spellathon puzzle.
-Spellathon involves listing all possible words from 7 given alphabets. 
No other alphabet is used.
-One alphabet should exist in each word (the alphabet in the center, Z,
 in following example).
-Minimum word length is four letters.
-If a letter repeats in the alphabet list, the letter can repeat same 
number of times in the word.
-At least 1 word should be a 7 letter word, using all 7 given alphabets.

-----B------
-A-------C--
-----Z------
-F-------D--
-----E------

Code in this file helps in generating and solving Spellathon puzzles.

TO DO: 
-exception and error handling
-use global constants for magic values
-split allthon and spellathon code cleanly
'''

import os
import sys

'''
CONSTANTS
'''
DATA_FILE_PATH = './games/spellathon/data'     #All data files are stored in this folder
TEMP_FOLDER = 'temp' #All temp files are here
DATA_FILE_WORDS = 'words.txt'           #First input file with word list
DATA_FILE_LONGWORDS = 'long_words.txt'  #Derived from input file, words.txt
FOLDER_SEPARATOR = '/'                  #Folder path separator used in Windows - use system var
TEMP_FILE_PREFIX = 'temp_file'          #Common prefix used for generating temp files

SPELLATHON_WORD_LENGTH_MIN = 4          #Minimum length of words used in spellathon
SPELLATHON_WORD_LENGTH_MAX = 7          #Maximum length of words used in spellathon
LEWAND_ALPHABETS = 'etaoinshrdlcumwfgypbvkjxqz' #average frequency of word usage

'''
Common functions
'''

'''
parseWordListAndSaveWords - checks each word in input file for occurrence
 of a character, and saves these words in a new file.
 
file_name_with_path - file name with words to filter
temp_file_name - file name of file created with filtered words
char_to_search - character to search, in each word, in the input file
'''
def parseWordListAndSaveWords(file_name_with_path, temp_file_name, 
                              char_to_search):
    words = open(file_name_with_path, 'r')
    
    char_words = open(DATA_FILE_PATH + FOLDER_SEPARATOR + TEMP_FOLDER + FOLDER_SEPARATOR + temp_file_name, 'w')
        
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
    
    print("Char: {}, Lines read: {}, Lines written: {}".format( 
        char_to_search, readLines, writtenLines))
    
    words.close()
    char_words.close()

    
'''
Sorts list in reverse order, based on occurrence in Lewand's alphabets
 (alphabet frequency).
This helps in short-listing the words faster
'''
def sortSearchLettersAsPerFrequency(alphabetList):
    returnList = sorted(list(alphabetList), key = lambda x: LEWAND_ALPHABETS.index(x))
    return returnList[::-1]

'''
parseWordListAndSaveLongWords - following function parses word list file,
 and generates a new file containing words of length 7 or more. Used for 
 finding words which contain all 7 letters.
 File parsed is './../data/words.txt' and file generated is 
'./../data/long_words.txt'

file_name_with_path - input file to parse for words, one word in each line
word_length_to_filter - words of length longer that this number are filtered
into a new file
'''
def parseWordListAndSaveLongWords(file_name_with_path, word_length_to_filter):
    try:
        words = open(file_name_with_path, 'r')
    except FileNotFoundError:
        print('File not found. A list of words, with a word in each line, should exist: ' + file_name_with_path)
        return
    
    #words longer than word_length_to_filter are saved in following file
    long_words = open(DATA_FILE_PATH + FOLDER_SEPARATOR + TEMP_FOLDER + FOLDER_SEPARATOR + DATA_FILE_LONGWORDS, 'w')
        
    readLines = 0
    writtenLines = 0
    
    #loop through the input file words, and save long words in new file, long_words.txt
    while True:
        line = words.readline()
        
        if not line:
            break
        readLines += 1
        final_line = line.strip()
        if len(final_line) >= word_length_to_filter:
            long_words.writelines( final_line + '\n')
            writtenLines += 1
    
    print("Lines read: {}, Lines written: {}".format( readLines, writtenLines))
    
    words.close()
    long_words.close()


'''
parseWordListOfGivenLength - following function parses word list file,
 and generates a new file containing words of length 4 to 7.
 
 File parsed is './../data/words.txt' and file generated is './../data/given_words.txt'

file_name_with_path - input file to parse for words, one word in each line
min_length_to_filter, max_length_to_filter - words of length between min and max are filtered
into a new file
leading_alphabet - alphabet which should exist in each word
'''
def parseWordListOfGivenLength( file_name_with_path, min_length_to_filter, 
                                max_length_to_filter, leading_alphabet):
    try:
        words = open(file_name_with_path, 'r')
    except FileNotFoundError:
        print('File not found. A list of words, with a word in each line, should exist: ' + file_name_with_path)
        return
    
    #words longer than word_length_to_filter are saved in following file
    long_words = open(DATA_FILE_PATH + FOLDER_SEPARATOR + TEMP_FOLDER + FOLDER_SEPARATOR + DATA_FILE_LONGWORDS, 'w')
        
    readLines = 0
    writtenLines = 0
    
    #loop through the input file words, and save long words in new file, long_words.txt
    while True:
        line = words.readline()
        
        if not line:
            break
        readLines += 1
        final_line = line.strip()
        if len(final_line) >= min_length_to_filter and len(final_line) <= max_length_to_filter and leading_alphabet in final_line:
            long_words.writelines( final_line + '\n')
            writtenLines += 1
    
    print("Lines read: {}, Lines written: {}".format( readLines, writtenLines))
    
    words.close()
    long_words.close()


'''
------------------------------------------------------------------------
Variation of Spellathon: Allthon

This section contains code for finding words that contain all the given input
letters. Other letters can also occur in the words. 
------------------------------------------------------------------------
'''

'''
findWordsWithAllAlphabetsSimpleSearch takes a string with 7/etc letters with 
which words need to be created (other letters can exist).

This function implements a simple logic, and other version will try to
 implement an optimized solution and/or use regex.
 
NOTE: This function does not exactly solve spellathon, but finds words 
which use all input letters.

Assumptions:
-First alphabet in the string is the central letter, which needs to 
occur in each word.
-This function assumes that a file exists, ./../data/words.txt, 
which contains all the words that should be used for solving this puzzle.
-Code assumes a temp folder exists in path './../data/temp', and it 
is used for storing temporary files
-This version assumes all chars are unique, and future version will 
handle duplicate chars.
-Lewand list of alphabets for most common to least common alphabets 
in appearance is used, to shortlist the word list faster: 
etaoinshrdlcumwfgypbvkjxqz
( https://en.wikipedia.org/wiki/Letter_frequency )
'''
def findWordsWithAllAlphabetsSimpleSearch(alphabetList):
    
    alphabet_length = len(alphabetList)

    #Create file with all words longer than length alphabetlist length
    parseWordListAndSaveLongWords(DATA_FILE_PATH + FOLDER_SEPARATOR + DATA_FILE_WORDS, alphabet_length)
    
    #initialize temp file names, for each alphabet 1 file is created
    temp_file_names = [TEMP_FILE_PREFIX +str(x) for x in range(alphabet_length)] 
    
    #TODO: Following code is really for spellathon, and needs to move there. Allthon searches for all words
    #parseWordListAndSaveWords(DATA_FILE_PATH + FOLDER_SEPARATOR + DATA_FILE_LONGWORDS, 
    #                          temp_file_names[0], alphabetList[0])
    
    #sort the list of alphabets based on occurrence to filter words faster
    #filtering least used words first
    sorted_alphabets = sortSearchLettersAsPerFrequency(alphabetList)
    
    #start with input file
    previous_temp_file = DATA_FILE_LONGWORDS
    
    for char_to_search, temp_file in zip(sorted_alphabets, temp_file_names):
        parseWordListAndSaveWords(DATA_FILE_PATH + FOLDER_SEPARATOR + TEMP_FOLDER 
                                    + FOLDER_SEPARATOR 
                                    + previous_temp_file, temp_file, char_to_search)
        previous_temp_file = temp_file
    
    #Read final file, extract the shortlisted words and print them
    final_word_file = open(DATA_FILE_PATH + FOLDER_SEPARATOR + TEMP_FOLDER 
                                    + FOLDER_SEPARATOR + temp_file_names[-1], 'r')
    
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
------------------------------------------------------------------------
Spellathon

This section contains code for finding words for spellathon.

Overall logic for finding the words:
-Find words of length 4, 5, 6 and 7 - generate 4 temporary files.
-Find all possible combinations of 7 letters, contain 4, 5, 6 and 7 
letters (only 1 combination of all 7 letters exists).
-Find all words which only contain any of the possible combinations.
------------------------------------------------------------------------
'''

'''
findWordsForSpellathonSimpleSearch takes a string with 7 letters with 
which words need to be created.

This function implements a simple logic, and other version will try to
 implement an optimized solution and/or use regex.
 
Assumptions:
-First alphabet in the string is the central letter, which needs to 
occur in each word.
-This function assumes that a file exists, ./../data/words.txt, 
which contains all the words that should be used for solving this puzzle.
-Code assumes a temp folder exists in path './../data/temp', and it 
is used for storing temporary files
-This version assumes all chars are unique, and future version will 
handle duplicate chars.
-Lewand list of alphabets for most common to least common alphabets 
in appearance is used, to shortlist the word list faster: 
etaoinshrdlcumwfgypbvkjxqz
( https://en.wikipedia.org/wiki/Letter_frequency )
'''
def findWordsForSpellathonSimpleSearch(alphabetList):
    '''
    1. Find words of length between 4 and 7, both inclusive, because in spellathon
    we can only use the given letters
    2. Find all combinations of letters which are of length 4 to 7
    3. Find words which are made up of only letters in any of the above combinations
    '''
    #Create file with all words between length 4-7, and leading alphabet (alphabet which should exist in each word)
    parseWordListOfGivenLength( DATA_FILE_PATH + FOLDER_SEPARATOR + DATA_FILE_WORDS, 
                                SPELLATHON_WORD_LENGTH_MIN, 
                                SPELLATHON_WORD_LENGTH_MAX,
                                alphabetList[0])

    #TODO


if __name__ == '__main__':
    print('Working directory: ' + os.getcwd())

    function = input('Function to execute (1 for allthon, 2 for spellathon): ')
    alphabets = input('Input related alphabet list (any number of alphabets for 1, 7 alphabets for 2): ')

    try:
        if function == '1':
            findWordsWithAllAlphabetsSimpleSearch(alphabets)
        elif function == '2':
            if len(alphabets) == 7:
                findWordsForSpellathonSimpleSearch(alphabets)
            else:
                print('Alphabet list should be 7 characters long')
        else:
            print('wrong function selection: ' + function)
    except:
        print(sys.exc_info()[0])
    print('end')
        
    