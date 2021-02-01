'''
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
validTime(time) = true;
For time = "25:51", the output should be
validTime(time) = false;
For time = "02:76", the output should be
validTime(time) = false.'''


def validTime(time):
    time_split= time.split(':')
    return int(time_split[0])<=23 and int(time_split[1])<=59

def validTime2(time):
    h,m=map(int,time.split(":"))
    return 0<=h<24 and 0<=m<60