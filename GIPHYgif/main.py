import urllib,json
from bs4 import BeautifulSoup

base_url = urllib.urlopen('http://api.giphy.com/v1/gifs/search?q=funny+cat&api_key=dc6zaTOxFJmzC')
soup_data = BeautifulSoup(base_url,"html.parser")
data = json.loads(soup_data)
print data['data']
