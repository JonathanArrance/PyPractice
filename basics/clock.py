#Given a time in 12-hour AM/PM format, convert it to 24-hour military time. 12:00:00AM on a 12-hour clock is 00:00:00 
#on a 24-hour clock. 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock. For example, if s = 12:01:00AM, return 00:01:00

"""
Everything after 12 is just adding an hour

There is a special case for midnight
12:01AM = 00:01
11:59AM = 23:59
12:00PM(noon) = 12:00 
PM will indicate if we add an hour or just keep count
01:00PM = 13:00



"""

def converttime(timein):
    
    #look at the last two Chars on the string
    m = timein[-2:]
    hour = timein[:2]
    minsec = timein[2:-2]

    if str(m).upper() == 'AM' and int(hour) == 12:
        return '00'+ minsec
    elif str(m).upper() == 'PM' and int(hour) != 12:
        x = int(hour) + 12
        return str(x) + minsec
    elif str(m).upper() == 'PM' and int(hour) == 12:
        return hour + minsec
    else:
        return hour + minsec

T='12:59:00PM'
T2='12:01:00AM'
T3='01:00:00PM'
T4='11:59:00PM'

print(converttime(T4))