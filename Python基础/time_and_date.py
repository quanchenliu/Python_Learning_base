import time
print(time.time())  # 1970年1月1日0分0秒至今 所经历的秒数, 又称为时间戳

t = time.localtime()
print(time.localtime())

# Y: 年份（四位数）        %y: 年份（两位数）     %m: 月份               %d: 日期
# %H: 小时（24小时制）     %I: 小时（12小时制）   %M: 分钟               %S: 秒
s = time.strftime('%a %b %d %I:%M%p %Y', t)
print(s)
print('/////////////////time model//////////////////')

from datetime import date
d = date.today()
print('今天是{}'.format(d))                              # 输出年、月、日
print('{}是星期{}'.format(d, date.weekday(d)))           # 返回该日期是星期几（0是星期一）
print('{}是星期{}'.format(d, date.isoweekday(d)))        # 返回该日期是星期几（1是星期一）
print(d.strftime("%Y-%m-%d"))                           # 将日期格式化为字符串


print('/////////////////datetime model//////////////////')
