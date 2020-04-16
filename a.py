import requests
import re
url = 'https://www.qiushibaike.com/8hr/page/2/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
res = requests.get(url,headers = header)
info = res.text
a = re.findall(r'<a.+>(.+)</a>',info)
c = re.findall(r'img.+alt=(.+)>',info)
with open('hh.txt','w',encoding='utf-8') as f:
    for i in a:
        f.write(i+"\n\n\n")