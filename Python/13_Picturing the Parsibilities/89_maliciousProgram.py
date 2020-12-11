'''
You decided to create a malicious program to play a joke on your friend. He's now struggling with a report for his work, and you want to scare him by spoiling some dates in it (of course you will change them back after you have your moment of joy). However, you don't want him to discover the errors until he starts double-checking the report, so all spoiled dates should be valid.

Now your goal is to write a program that modifies the curDate according to the rules that specify the changes that should be made. However, if the changes result in an incorrect date, the program should leave the date as is.

Given the changes and the curDate, return the spoiled date or don't change it if the result appears to be invalid.

Example

For curDate = "01 Jul 2016 16:53:24" and
changes = [2, 3, -1, 0, 5, 4], the output should be
maliciousProgram(curDate, changes) = "03 Oct 2015 16:58:28";

For curDate = "15 Mar 1998 12:09:59" and
changes = [-2, 0, 9, 1, 3, 1], the output should be
maliciousProgram(curDate, changes) = "15 Mar 1998 12:09:59".

After changing the date will look like "13 Mar 2007 13:12:60", which is incorrect, because the number of seconds cannot be equal to 60
'''
from datetime import datetime
def maliciousProgram(curDate, changes):

    mytime = datetime.strptime(curDate, '%d %b %Y %H:%M:%S')
    try:
        new_time = mytime.replace(
            day = mytime.day + changes[0],
            month = mytime.month + changes[1],
            year = mytime.year + changes[2],
            hour = mytime.hour + changes[3],
            minute = mytime.minute + changes[4],
            second = mytime.second + changes[5]
            )
    except ValueError:
        return curDate
   
    return new_time.strftime("%d %b %Y %H:%M:%S")

'''
from datetime import datetime
import operator

def maliciousProgram(curDate, changes):
    date = datetime.strptime(curDate, '%d %b %Y %H:%M:%S')
    fields = [date.year, date.month, date.day, date.hour, date.minute, date.second]
    changes[:3] = changes[2::-1]
    modFields = map(operator.add, fields, changes)
    try:
        modDate = datetime(*modFields).strftime('%d %b %Y %H:%M:%S')
        return modDate
    except ValueError:
        return curDate
        '''