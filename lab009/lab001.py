# coding:utf8

import re

line = '<script src="/twell/flight/inter/js/1542165209052"></script>'
m = re.search(r'twell', line, re.M | re.I)
print("m=", m.span())
a,b = m.span()
print(line[a:b])

print(re.match(r'com', 'www.runoob.com'))

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"
