import datetime

print(dir(datetime))

datetime_object = datetime.datetime.now()
print('datetime.datetime.now(): ' + str(datetime_object))

datetime_object1 = datetime.date.today()
print('datetime.date.today(): ' + str(datetime_object1))


a = 2025
b = 5
c = 27
date = datetime.date(a,b,c)
print('datetime.date(2025, 5, 27): ' +str(date))

from datetime import date

today = date.today()
print('Current date: ', today)
print('Current year: ', today.year)
print('Current month: ', today.month)
print('Current day: ', today.day)

timestamp = date.fromtimestamp(937538688)
print('Date = ', timestamp)


from datetime import time

a = time(11,34,56)
print('time(11,34,56) = ', a)

from datetime import datetime

b = datetime(2025,11,26,9,30,25)
print('datetime(2025,11,26,9,30,25) = ', b)
print('year', b.year)
print('hour', b.hour)

a = date(2025, 2, 10)
b = date(2025, 1, 10)
print(b-a)

print('date formats')
now = datetime.now()
print('now.strftime(\'%h:%m:%s\'): ', now.strftime('%H:%M:%S'))
print("now.strftime('%d/%m/%Y $H:%M:S'): ", now.strftime('%d/%m/%Y $H:%M:S'))

from datetime import timedelta

t1 = timedelta(weeks = 4, days = 9, hours = 2, seconds = 44)
t2 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 10)
print(t1-t2)
print (t1, 'is equal to ' , t1.total_seconds(), 's')



