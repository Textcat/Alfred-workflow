# -*- coding: utf-8 -*-
import re,urllib,sys
from bs4 import BeautifulSoup
base_url = urllib.urlopen('http://baike.baidu.com/search?word={query}')
soup_data = BeautifulSoup(base_url)

result = [u'<?xml version="1.0"?>', u'<items>']
my_list = soup_data.find_all('a','result-title')
for id_count in range(len(my_list)):
    result_url = my_list[id_count].get('href')
    title = my_list[id_count].get_text().encode('utf-8').replace(' ','')
    result.append(u'<item uid="baikesearch' + str(id_count) + u'" arg="' + result_url + u'">')
    result.append(u'<title>' + title.decode("utf8") + u'</title>')
    result.append(u'<subtitle>'+'打开这条百科'.decode("utf8")+u'</subtitle>')
    result.append(u'<icon>baike.png</icon>')
    result.append(u'</item>')

result.append(u'</items>')
xml = ''.join(result)

print xml.encode('utf-8')