# coding:utf8


import urllib

a = "上海"
a1 = urllib.quote(a)
print (a1)

b = urllib.unquote(a1)
print(b)
