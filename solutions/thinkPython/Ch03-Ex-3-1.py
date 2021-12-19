import os

def right_justify(input):
    print(' '*(70-len(input)) + input, end='\n')

def right_justify_visual_test():
    print('-'*70, end='\n')       #gives visual indication of 70 characters for comparison

if __name__ == '__main__':
    right_justify(input('Type text to right justify: ').strip())
    right_justify_visual_test()