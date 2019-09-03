import datetime
import calendar
import time
mb=datetime.date(2002, 10, 16)
nb=datetime.date(2019, 10, 16)
now=datetime.date.today()
print(mb)
print(mb.year)
print(mb.month)
print(mb.day)
print(mb.weekday)
print(nb-now)
cal = calendar.month(2017, 5)
print(cal)
dt = datetime.timedelta(days = 1)
yd = now-dt
print(yd)
yd+=2*dt
print(yd)
yd-=3*dt
print(yd)
