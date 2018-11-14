# coding:utf8

a = "hello world123"
i = a.rindex("l")
print("i=", i)

a = a[:i + 1] + "!" + a[i + 1:]
print(a)
print(len(a))