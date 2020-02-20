# coding:utf8

import re

line = "价格:￥2499.00元"
matchObj = re.findall(r'[0-9]*\.?[0-9]+', line, re.M | re.I)
if matchObj:
    print(matchObj)
else:
    print "No match!!"




