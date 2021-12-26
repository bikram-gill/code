'''
File contains different functions to find palindromic words.
'''
import os
import sys

'''
findAllPalindromes - finds all palindromes in input file containing 
one word in each line.
'''
def findAllPalindromes(input_file_words, output_file_palindrome_words):

    words = open(input_file_words, 'r')
    output_words = open(output_file_palindrome_words, 'w')
    
    total_words = 0
    num_of_words = 0

    while True:
        line = words.readline().strip()
        if not line:
            break
        total_words += 1
        
        if line == line[::-1]:
            output_words.writelines(line + '\n')
            num_of_words += 1

    words.close()
    output_words.close()

    print('Words read: ' + str(total_words))

    return num_of_words

'''
findLongestPalindromes - finds all palindromes in input file containing 
one word in each line, and having maximum length.
'''
def findLongestPalindromes(input_file_words, output_file_palindrome_words):

    words = open(input_file_words, 'r')
    output_words = open(output_file_palindrome_words, 'w')
    
    total_words = 0
    num_of_palindromes = 0
    num_of_long_palindromes = 0
    palindromes = []
    max_palindrome_length = 0

    while True:
        line = words.readline().strip()
        if not line:
            break
        total_words += 1
        
        if line == line[::-1]:
            palindromes.append(line)
            
            num_of_palindromes += 1

            if(max_palindrome_length < len(line)):
                max_palindrome_length = len(line)

    for word in [long_word for long_word in palindromes if len(long_word) == max_palindrome_length]:
        output_words.writelines(word + '\n')
        num_of_long_palindromes += 1

    words.close()
    output_words.close()

    print('Words read: ' + str(total_words))
    print('Palindromes read: ' + str(num_of_palindromes))
    print('Long palindromes read: ' + str(num_of_long_palindromes))

    return num_of_long_palindromes

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
\code\games\spellathon\python>python ./palindrome.py ../data/words.txt  ../data/temp/palindromes.txt

To print words, pass -p argument: 
\code\games\spellathon\python>python ./palindrome.py ../data/words.txt  ../data/temp/palindromes.txt -p

To find longest palindromes, pass -l argument:
\code\games\spellathon\python>python ./palindrome.py ../data/words.txt  ../data/temp/palindromes.txt -p -l
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
        output_file_words = './games/spellathon/data/temp/palindromes.txt'
    
    if sys.argv.__contains__('-l'):
        print('Number of long palindrome words found: ' + str(findLongestPalindromes(input_file_words, output_file_words)) )
    else:
        print('Number of palindrome words found: ' + str(findAllPalindromes(input_file_words, output_file_words)) )

    if sys.argv.__contains__('-p'):
        printWordsFromFile(output_file_words)
