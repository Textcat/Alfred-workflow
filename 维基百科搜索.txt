# -*- coding: utf-8 -*-

result = [u'<?xml version="1.0"?>', u'<items>']
result_url = u'https://zh.wikipedia.org/wiki/{query}'
result.append(u'<item uid="wikisearch' +  u'" arg="' + result_url + u'">')
result.append(u'<title>' + '探索这篇百科'.decode("utf8") + u'</title>')
result.append(u'<subtitle>'+'打开'.decode("utf8")+u'</subtitle>')
result.append(u'<icon>wiki.png</icon>')
result.append(u'</item>')

result.append(u'</items>')
xml = ''.join(result)
print xml.encode('utf-8')