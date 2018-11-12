# coding:utf8

import os

result = os.popen('node ' + "lab.js").read()
print("result={}".format(result))
