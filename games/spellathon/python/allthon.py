'''
File contains different functions to find words with different combinations 
of input letters.
'''
import os
import sys
import re
import string

'''
findWordsWithAllLetters - finds all words in input file, where each word 
contains all input letters.
'''
def findWordsWithAllLetters(input_letters, input_file_words, output_file_palindrome_words, allow_char_repetition):

    words = open(input_file_words, 'r')
    output_words = open(output_file_palindrome_words, 'w')
    
    total_words = 0
    num_of_words = 0
    
    #pattern to avoid repetition of characters
    repeat_pattern = r'(['+ input_letters + r']).*\1'

    while True:
        line = words.readline().strip()
        if not line:
            break
        total_words += 1
        
        if   (allow_char_repetition or None == re.search(repeat_pattern, line) ) and \
            all([x in line for x in input_letters]):
            output_words.writelines(line + '\n')
            num_of_words += 1

    words.close()
    output_words.close()

    print('Words read: ' + str(total_words))

    return num_of_words

'''
findWordsWithAllLettersInSequence - finds all words in input file, where each word 
contains all input letters, occuring in same sequence as in input.
'''
def findWordsWithAllLettersInSequence(input_letters, input_file_words, output_file_palindrome_words, allow_char_repetition):

    words = open(input_file_words, 'r')
    output_words = open(output_file_palindrome_words, 'w')
    
    total_words = 0
    num_of_words = 0
    
    #pattern for alphabets occuring in sequence, allows repetition
    delimiter = ''
    pattern = r''
    if allow_char_repetition:
        for ch in input_letters:
            pattern = pattern + delimiter + ch
            delimiter = r'.*'
    else:
        #pattern to avoid repetition of characters
        remaining_alphabets = re.sub('['+input_letters+']', '', string.ascii_lowercase)
        #pattern for alphabets occuring in sequence, does not allow repetition
        delimiter = r'['+remaining_alphabets+r']*'
        pattern = r'^' + delimiter
        for ch in input_letters:
            pattern = pattern + delimiter + ch
        pattern += delimiter + '$'  

    while True:
        line = words.readline().strip()
        if not line:
            break
        total_words += 1
        
        if   None != re.search(pattern, line) :
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
\code\games\spellathon\python>python ./allthon.py ../data/words.txt  ../data/temp/allletters.txt abcd

To print words, pass -p argument: 
\code\games\spellathon\python>python ./allthon.py ../data/words.txt  ../data/temp/allletters.txt abcd -p

Other arguments (mutually exclusive):
-o - find words made up of only input letters
-a - find words containing all input letters, without repetition
-ar - find words containing all input letters, with possible char repetition
-s - find words containing all input letters in sequence, without repetition
-sr - find words containing all input letters in sequence, with possible char repetition
'''
if __name__ == '__main__':
    print('Working directory: ' + os.getcwd())

    n = len(sys.argv)
    print("Total arguments passed:", n)
    if n >= 2:
        input_file_words = sys.argv[1] #First argument is always input file with complete path
        output_file_words = sys.argv[2] #Second argument is always output file with complete path
        input_letters = sys.argv[3] #Third argument is always input letters to search
    else:
        input_file_words = './games/spellathon/data/words.txt'
        output_file_words = './games/spellathon/data/temp/allletters.txt'
        input_letters = 'abcd'
    
    print(input_file_words, output_file_words, input_letters)

    if sys.argv.__contains__('-o'):
        #print('Number of words made up of input letters: ' + str(findWordsWithOnlyInputLetters(input_file_words, output_file_words)) )
        pass
    elif sys.argv.__contains__('-ar'):
        print('Number of words containing ALL input letters (with char repetition): ' 
                                + str(findWordsWithAllLetters(input_letters, input_file_words, output_file_words, True)) )
    elif sys.argv.__contains__('-a'):
        print('Number of words containing ALL input letters (without char repetition): ' 
                                + str(findWordsWithAllLetters(input_letters, input_file_words, output_file_words, False)) )
    elif sys.argv.__contains__('-sr'):
        print('Number of words containing ALL input letters in sequence (with char repetition): ' 
                                + str(findWordsWithAllLettersInSequence(input_letters, input_file_words, output_file_words, True)) )
    elif sys.argv.__contains__('-s'):
        print('Number of words containing ALL input letters in sequence (without char repetition): ' 
                                + str(findWordsWithAllLettersInSequence(input_letters, input_file_words, output_file_words, False)) )

    if sys.argv.__contains__('-p'):
        printWordsFromFile(output_file_words)