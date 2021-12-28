'''
Find n adjacent digits (e.g. 13), in a m digit number (e.g. 1000), which have the highest product.

NOTE: Write a version with prefix array, for possibly faster computation
'''

from datetime import datetime
import math

def largestProductInSeries(adjacentDigits, inputNumber):

    inputNumberStr = str(inputNumber)

    start = 0
    end = start + adjacentDigits
    max_combinations = len(inputNumberStr) - adjacentDigits
      
    maxProduct = 0
    for _ in range(max_combinations-1):  
        
        nextProduct = math.prod(list( map(int, [x for x in inputNumberStr[start: end]] ) ) )

        if maxProduct < nextProduct:
            maxProduct = nextProduct

        start += 1
        end += 1

    return maxProduct

if __name__ == '__main__':
    n = int (input('Input adjacent digits (E.g. 13): ') )
    
    #Change to read from input
    thousandDigitNumber =   '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843' + \
                            '8586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557' + \
                            '6689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749' + \
                            '3035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776' + \
                            '6572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397' + \
                            '5369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474' + \
                            '8216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586' + \
                            '1786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408' + \
                            '0719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606' + \
                            '0588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(largestProductInSeries( n,  thousandDigitNumber) ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )