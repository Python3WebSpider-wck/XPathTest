from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a')
result = html.xpath('//li')
print(result)
print(result[0])
