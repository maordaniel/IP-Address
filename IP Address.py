from urllib.request import *
from bs4 import BeautifulSoup

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                  'Chrome/60.0.3112.113 Safari/537.36 '
req = Request('https://www.whatsmyip.org/', headers=headers)
soup = urlopen(req)
xml = BeautifulSoup(soup, 'xml')
ip = xml.find("span", id="ip").text

# print(xml)
print('-'*24,'\n', '  Your Ip Address is :')
print('    ', ''.join(ip))
print('-'*24)
try:
    while True:
        pass
except KeyboardInterrupt:
    pass
