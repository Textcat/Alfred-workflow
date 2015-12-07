# -*- coding: utf-8 -*-
import re,urllib,sys
from bs4 import BeautifulSoup
base_url = urllib.urlopen('http://sspai.com')
soup_data = BeautifulSoup(base_url)

result = [u'<?xml version="1.0"?>', u'<items>']
my_list = soup_data.find_all('h2','title')
for id_count in range(len(my_list)):
    result_url =soup_data('h2','title')[id_count]('a')[0].get('href')
    title = my_list[id_count]('a')[0].get_text().encode('utf-8').replace('\n','').replace(' ','')
    result.append(u'<item uid="sspaiarticle' + str(id_count) + u'" arg="' + result_url + u'">')
    result.append(u'<title>' + title.decode("utf8") + u'</title>')
    result.append(u'<subtitle>'+'打开这篇文章'.decode('utf8')+u'</subtitle>')
    result.append(u'<icon>sspai.png</icon>')
    result.append(u'</item>')

result.append(u'</items>')
xml = ''.join(result)

print xml.encode('utf-8')