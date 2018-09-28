import calendar
import time

cal=calendar.month(2018,9)
print(cal)

print(time.strftime("%a %b %d %H:%S:%Y",time.localtime()))

money=100
def Add(*value,age,name="cc"):
# 全局变量的使用
  global money
  money=money+1
  print(money)
# 有默认值的参数
  print(f"{name} is {age}")
# 不定长参数的使用
  for i in value:
    print(i)

print(money)
# 关键词参数的使用
Add(1,2,3,age=4)
