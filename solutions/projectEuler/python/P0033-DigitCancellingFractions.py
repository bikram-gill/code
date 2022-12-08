'''
Find 2 digit fractions, less than 1, so that on digit cancellation it's value does not change
TODO: 
'''

from datetime import datetime
import os

def digitCancellingFranctions():

    num = 1
    den = 1
    
    for i in range(11,99):
        for j in range(i+1, 99):
            f1 = i / j

            #cancel digits
            for k in list(str(i)):

                if (j%10 == 0 and i%10 ==0):
                    continue

                i2 = str(i)
                j2 = str(j)
                
                i3 = i2.replace(k,'')
                j3 = j2.replace(k,'')

                if(j3 == '0' or i3 == '' or j3 == ''):
                    continue

                f2 = int(i3) / int(j3)

                if(f1 == f2):
                    print(i,'/',j)
                    print(i3,'/',j3)

                    num *= int(i3)
                    den *= int(j3)

    
    for x in reversed(range(1,den)):
        if(num%x == 0 and den%x == 0):
            num /= x
            den /= x

    return den
    
if __name__ == '__main__':
    
    print(os.getcwd())
    
    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str(digitCancellingFranctions() ) )

    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )