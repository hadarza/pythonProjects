from datetime import datetime, timedelta

def isLeafYear(year) :
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def getYear(year):
    if(isLeafYear(year)):
        return regularYear
    else:
        return leapYear


def calcDays(date1,date2):

    def sortDates():
        if(date1[0] > date2[0]):
            return date2,date1
        if(date1[0] < date2[0]):
            return date1,date2
        if(date1[1] > date2[1]):  
            return date2,date1
        if(date1[1] < date2[1]):
            return date1,date2
        if(date1[2] > date2[2]):
            return date2,date1
        if(date1[2] < date2[2]):
            return date1,date2
        else:
            return date1,date2
        
    dt1 , dt2 = sortDates()

    y1 = dt1[0]
    m1 = dt1[1]
    d1 = dt1[2]

    y2 = dt2[0]
    m2 = dt2[1]
    d2 = dt2[2]

    sum = 0
    for year in range(y1,y2):
        if(isLeafYear(year)):
            sum += 366
        else :
            sum += 365

    dayInMonth = getYear(y1)
    for month in range(m1): # from 0 to m1-1
        sum -= dayInMonth[month]
    sum -= d1

    dayInMonth = getYear(y2)
    for month in range(m2): # from 0 to m2-1
        sum += dayInMonth[month]
    sum += d2

    return sum


regularYear = [0,31,28,31,30,31,30,31,31,30,31,30,31]
leapYear =    [0,31,29,31,30,31,30,31,31,30,31,30,31]

date1 = (2020,3,4)
date2 = (2023,8,12)
print(calcDays(date1,date2))
