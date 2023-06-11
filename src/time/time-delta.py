from datetime import datetime, timedelta

newyear = datetime(2023, 1, 1, 12)
print(f'new year moon is {newyear}')

now1 = datetime.now()
print(f'now is {now1}')

delta = now1 - newyear
print(f'delta is {delta}')

''' Result:
new year moon is 2023-01-01 12:00:00
now is 2023-06-11 21:02:43.981520
delta is 161 days, 9:02:43.981520
'''
