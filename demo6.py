from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//ul/a')
print(result)
if len(result) != 0:
    print(result[0])
