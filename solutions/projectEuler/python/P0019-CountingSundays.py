'''
How many Sundays fell on the first of the month between 2 dates (1 Jan 1901 to 31 Dec 2000)?
'''
import os
from datetime import datetime, date, timedelta

def countingSundays( d1, m1, y1, d2, m2, y2):

    d1 = date(y1, m1, d1)
    d2 = date(y2, m2, d2)
    td = timedelta(days=1)

    count = 0
    while(d1 <= d2):
        #check 1st and sunday
        if d1.day == 1 and d1.weekday() == 6:
            count += 1
        d1 = d1 + td

    return count

if __name__ == '__main__':
     
    print(os.getcwd())
    
    d1, m1, y1 = list(map( int, input('Input start date, day month year (e.g. 1 1 1901): ').split() ) )
    d2, m2, y2 = list(map( int, input('Input end date, day month year (e.g. 31 12 2000): ').split() ) )

    start = datetime.now().strftime("%H:%M:%S")

    print('Answer: ', str( countingSundays( d1, m1, y1, d2, m2, y2) ) )
    
    end = datetime.now().strftime("%H:%M:%S")

    print( 'Start and end time: ', start, ' ', end )