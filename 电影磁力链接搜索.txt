# -*- coding: utf-8 -*-
import re,urllib,sys
from bs4 import BeautifulSoup
base_url = urllib.urlopen('http://www.dianyingll.com/s?k={query}')
soup_data = BeautifulSoup(base_url)


result = [u'<?xml version="1.0"?>', u'<items>']
my_list = soup_data.find_all('a',id='magnet_id')
for id_count in range(len(my_list)):
    down_url = re.findall(r'magnet.*?&',my_list[id_count].get('href'))[0].replace('&','')
    title = re.findall(r'dn=.*',my_list[id_count].get('href'))[0].replace('dn=','').encode('utf8').replace('\xe3\x80\x91','').replace('\xe3\x80\x90','')
    subtitle = soup_data('p','tail')[id_count]('span')[2].get_text().encode('utf8')
    result.append(u'<item uid="magnetsearch' + str(id_count) + u'" arg="' + down_url + u'">')
    result.append(u'<title>' + title.decode("utf8") + u'</title>')
    result.append(u'<subtitle>'+subtitle.decode("utf8")+u'</subtitle>')
    result.append(u'<icon>magnet.png</icon>')
    result.append(u'</item>')


result.append(u'</items>')
xml = ''.join(result)


print xml.encode('utf-8')