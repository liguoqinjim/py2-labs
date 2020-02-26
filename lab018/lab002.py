from lxml.etree import fromstring

xml = """<some>
<nodes>
<meta itemprop="price" content="4999.00"></meta>
</nodes>
</some>"""

doc = fromstring(xml)
print(doc.xpath('//meta[@itemprop="price"]/@content'))