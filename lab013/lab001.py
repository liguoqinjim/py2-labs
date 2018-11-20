# coding:utf8

import time
import datetime

t = time.time()

print (t)  # 原始时间数据
print (int(t))  # 秒级时间戳
print (int(round(t * 1000)))  # 毫秒级时间戳

nowTime = lambda: int(round(t * 1000))
print (nowTime())  # 毫秒级时间戳，基于lambda

print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 日期格式化

# 1542353949477
# 1542614205855
# 1542612603164

# 1542353949489

# print(1542612603 / 1000 / 30)
