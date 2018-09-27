import calendar
import time

cal=calendar.month(2018,9)
print(cal)

print(time.strftime("%a %b %d %H:%S:%Y",time.localtime()))
