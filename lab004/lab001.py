# coding:utf8

import json

with open('data/test.json', 'r') as f:
    d = json.load(f)
print(d)
print(d["a"])
