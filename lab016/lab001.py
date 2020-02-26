import demjson

# from
js_obj = '{x:1, y:2, z:3}'

# to
py_obj = demjson.decode(js_obj)
print(py_obj)
