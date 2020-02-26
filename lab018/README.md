# [lxml](https://github.com/lxml/lxml)

|实验|简介|说明|
|---|---|---|
|lab001|xpath example| |
|lab002|example||
|lab003|example||
|lab004|正则表达式，decode("utf-8")，注意lxml里面的tbody||

# 注意
 - 从文件读取的html可能会需要先调用decode("utf-8")才会被xpath查询出来
 - 需要注意lxml使用xpath的时候，遇到tbody的情况要是找不出元素的时候，可以去掉tbody试一下。