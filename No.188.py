import datetime


def getHappyNumber(day: int):
    strDay = str(day)
    sum = 0
    for i in range(len(strDay)):
        sum += int(strDay[i])
    return sum


current = datetime.datetime.strptime('2015/01/01', '%Y/%m/%d')
count = 0
while current.year == 2015:
    current = current + datetime.timedelta(days=1)
    happyNumber = getHappyNumber(current.day)
    if current.month == happyNumber:
        count += 1

print(count)
