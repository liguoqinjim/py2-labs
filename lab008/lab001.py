# coding:utf8

import os
import sys

result = os.popen('dir').read()
print("result={}".format(result.decode("gbk").encode("utf-8")))
