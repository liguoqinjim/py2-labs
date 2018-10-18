# coding:utf8

a = "上海"
print (a)

b = u"上海"
print (b)

c = a.decode("utf-8")
print c

if a.decode("utf-8") == b:
    print ("a==b")
