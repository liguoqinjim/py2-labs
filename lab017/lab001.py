#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json

print sys.getdefaultencoding()

a = "测试"
b = u"测试"

print a.decode('utf-8').encode('cp936')
print a.decode('utf-8').encode('gb2312')

print b.encode('utf-8')

print type(a), type(b)

c = {"city": "上海", "area": "黄浦"}
c1 = json.dumps(c)
c2 = json.dumps(c).decode("unicode-escape")
print(c1)
print(c1.encode("utf-8"))
print(c2)
