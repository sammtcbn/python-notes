import datetime

day1 = datetime.datetime.today()
print (day1)

day2 = day1.strftime('%Y-%m-%d')
print (day2)

day3 = day1.strftime("%Y%m%d_%H%M%S")
print (day3)
