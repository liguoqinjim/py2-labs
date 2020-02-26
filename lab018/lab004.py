#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import lxml.html
from lxml import etree

if __name__ == '__main__':
    # 读取文件
    with open('data/1.html', 'r') as f:
        data = f.read()

    html = etree.HTML(data.decode("utf-8"))
    # 所有<a>的href
    urls = html.xpath('//a/@href')
    print urls

    # //*[@id="item_663066"]
    item = html.xpath('//*[@id="item_663066"]/@width')
    print(item)

    # 正则
    items = html.xpath('//*[starts-with(@id,"item_")]')
    # items = html.xpath('//*[starts-with(@id,"item_")]/table/tbody  / tr / td /ul /li/ a')
    print(len(items))

    # 注意：lxml里面的tbody有点不对
    # 有tbody的在chrome的console中搜索是对的，但是lxml里面就是不对，加了tbody就会找不到
    # 下面的for循环里面也是都去掉了tbody
    print(html.xpath('//*[@id="item_663066"]/table/tbody/tr[1]/td/a/img'))
    print(html.xpath('//*[@id="item_663066"]/table/tr[1]/td/a/img'))

    for item in items:
        print("----------------")
        img = item.xpath("table/tr[1]/td/a/img/@src")
        print("src={}".format(img[0]))
        # document.querySelector("#item_663066 > table > tbody > tr:nth-child(2) > td > ul:nth-child(1) > li > a")
        # // *[ @ id = "item_663066"] / table / tbody / tr[2] / td / ul[1] / li / a
        title = item.xpath("table/tr[2]/td/ul[1]/li/a/text()")
        print("title={}".format(title[0].encode("utf-8")))
        url = item.xpath("table/tr[2]/td/ul[1]/li/a/@href")
        print("href={}".format(url[0]))

        # // *[ @ id = "item_663066"] / table / tbody / tr[2] / td / ul[2] / li / a
        company = item.xpath("table/tr[2]/td/ul[2]/li/a/text()")
        print(company)
        print("company={}".format(company[0].encode("utf-8")))

        company_url = item.xpath("table/tr[2]/td/ul[2]/li/a/@href")
        print("company_url={}".format(company_url))
