# -*- coding: utf-8 -*-
import re,urllib,sys
from bs4 import BeautifulSoup
base_url = urllib.urlopen('http://zhidao.baidu.com/index?word={query}')
soup_data = BeautifulSoup(base_url)

result = [u'<?xml version="1.0"?>', u'<items>']
my_list = soup_data.find_all('a','a2')
title2_data=soup_data.find_all('p',"mbotton n-fz")
for id_count in range(1,8):
    try:
        zhidao_id=(re.findall(r'[0-9]*\.',my_list[id_count].get('href'))[0]).replace('.','')
        result_url = u'http://zhidao.baidu.com/question/'+zhidao_id
        title = my_list[id_count].get_text().encode('utf-8')
        title2 = title2_data[id_count].get_text().encode('utf-8')
        result.append(u'<item uid="baidusearch' + str(id_count) + u'" arg="' + result_url + u'">')
        result.append(u'<title>' + title.decode("utf8") + u'</title>')
        result.append(u'<subtitle>'+title2.decode("utf8")+u'</subtitle>')
        result.append(u'<icon>zhidao.png</icon>')
        result.append(u'</item>')
    except:
        pass

result.append(u'</items>')
xml = ''.join(result)

print xml.encode('utf-8')