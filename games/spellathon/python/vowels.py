'''
File contains different functions to find words with different vowel combinations.

TODO: Optimize the functions into a single function, and parametrize comparision steps
'''
import os
import sys
import re
import string

'''
findWordsWithAllVowels - finds all words in input file, where each word 
contains all vowels.
'''
def findWordsWithAllVowels(input_file_words, output_file_palindrome_words, allow_char_repetition):

    words = open(input_file_words, 'r')
    output_words = open(output_file_palindrome_words, 'w')
    
    total_words = 0
    num_of_words = 0
    
    #pattern to avoid repetition of characters
    repeat_pattern = r'([aeiou]).*\1'

    while True:
        line = words.readline().strip()
        if not line:
            break
        total_words += 1
        
        if (allow_char_repetition or None == re.search(repeat_pattern, line) ) and \
            'a' in line and 'e' in line and 'i' in line and 'o' in line and 'u' in line :
            output_words.writelines(line + '\n')
            num_of_words += 1

    words.close()
    output_words.close()

    print('Words read: ' + str(total_words))

    return num_of_words

'''
findWordsWithAllVowelsInSequence - finds all words in input file, where each word 
contains all vowels. Each vowel should be present in sequence (aeiou).
'''
def findWordsWithAllVowelsInSequence(input_file_words, output_file_palindrome_words, allow_char_repetition):

    words = open(input_file_words, 'r')
    output_words = open(output_file_palindrome_words, 'w')
    
    total_words = 0
    num_of_words = 0
    
    #Create regex to search
    pattern = r'a.*e.*i.*o.*u'

    #pattern to avoid repetition of characters
    repeat_pattern = r'([aeiou]).*\1'

    while True:
        line = words.readline().strip()
        if not line:
            break
        total_words += 1
        
        if None != re.search(pattern, line) and (allow_char_repetition or None == re.search(repeat_pattern, line) ):
            output_words.writelines(line + '\n')
            num_of_words += 1

    words.close()
    output_words.close()

    print('Words read: ' + str(total_words))

    return num_of_words

'''
findWordsWithOnlyVowels - finds all words made up of only vowels.
'''
def findWordsWithOnlyVowels(input_file_words, output_file_palindrome_words):

    words = open(input_file_words, 'r')
    output_words = open(output_file_palindrome_words, 'w')
    
    total_words = 0
    num_of_words = 0
    
    #Find characters to exclude from words
    str_exclude = re.sub(r'[aeiou]','', string.ascii_lowercase)

    pattern_exclude = r'[' + str_exclude + ']'

    while True:
        line = words.readline().strip()
        if not line:
            break
        total_words += 1
        
        if None == re.search(pattern_exclude, line):
            output_words.writelines(line + '\n')
            num_of_words += 1

    words.close()
    output_words.close()

    print('Words read: ' + str(total_words))

    return num_of_words

'''
prints words from file.
'''
def printWordsFromFile(input_file_name):
    
    input_words = open(input_file_name, 'r')

    wordCount = 0

    while True:
        line = input_words.readline().strip()

        if not line:
            break
        
        wordCount += 1
        
        print(line, end=" ")
    
    print('\nTotal word count: ' + str(wordCount))

    input_words.close()


'''
To run this python file, pass input file containing words to process as first argument.
Each word should be present in a separate line.
For example, 
\code\games\spellathon\python>python ./palindrome.py ../data/words.txt  ../data/temp/vowels.txt

To print words, pass -p argument: 
\code\games\spellathon\python>python ./palindrome.py ../data/words.txt  ../data/temp/vowels.txt -p

Other arguments (mutually exclusive):
-o - find words made up of only vowels
-a - find words containing all vowels, without repetition
-ar - find words containing all vowels, with possible char repetition
-s - find words containing all vowels in sequence, aeiou, without repetition
-sr - find words containing all vowels in sequence, aeiou, with possible char repetition
'''
if __name__ == '__main__':
    print('Working directory: ' + os.getcwd())

    n = len(sys.argv)
    print("Total arguments passed:", n)
    if n >= 2:
        input_file_words = sys.argv[1] #First argument is always input file with complete path
        output_file_words = sys.argv[2] #Second argument is always output file with complete path
    else:
        input_file_words = './games/spellathon/data/words.txt'
        output_file_words = './games/spellathon/data/temp/vowels.txt'
    
    if sys.argv.__contains__('-o'):
        print('Number of words made up of vowels: ' 
                                + str(findWordsWithOnlyVowels(input_file_words, output_file_words)) )
    elif sys.argv.__contains__('-ar'):
        print('Number of words containing ALL vowels (with char repetition): ' 
                                + str(findWordsWithAllVowels(input_file_words, output_file_words, True)) )
    elif sys.argv.__contains__('-a'):
        print('Number of words containing ALL vowels (without char repetition): ' 
                                + str(findWordsWithAllVowels(input_file_words, output_file_words, False)) )
    elif sys.argv.__contains__('-sr'):
        print('Number of words containing ALL vowels in sequence (with char repetition): ' 
                                + str(findWordsWithAllVowelsInSequence(input_file_words, output_file_words, True)) )
    elif sys.argv.__contains__('-s'):
        print('Number of words containing ALL vowels in sequence (without char repetition): ' 
                                + str(findWordsWithAllVowelsInSequence(input_file_words, output_file_words, False)) )

    if sys.argv.__contains__('-p'):
        printWordsFromFile(output_file_words)