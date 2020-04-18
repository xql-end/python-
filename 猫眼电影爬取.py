import requests
from fake_useragent import UserAgent
import re
from lxml import etree

def analysis_xpath(resopen):
    e = etree.HTML(resopen)
    name = e.xpath('//dl[@class="movie-list"]//a[@data-act="movies-click"]/text()')
    tepy = e.xpath('//dd/div[@class="movie-item film-channel"]/div[@class="movie-item-hover"]/a/div[@class="movie-hover-info"]/div[@class="movie-hover-title"][2]/text()')
    rname = e.xpath('//dd/div[@class="movie-item film-channel"]/div[@class="movie-item-hover"]/a/div[@class="movie-hover-info"]/div[@class="movie-hover-title"][3]/text()')
    rnames = []
    tepys = []
    for i in range(1,len(tepy)):
        z = str(re.findall(r'\S+',tepy[i]))
        s = str(re.findall(r'\S+',rname[i]))
        tepys.append(z)
        rnames.append(s)
    with open('猫眼电影.txt','a',encoding='utf-8') as f:
        for i in range(len(name)):
            f.write("电影名："+name[i]+"\t"+"电影类型："+tepys[i]+"\t"+"演员"+rnames[i]+"\n")
def pa(url):
    header = {
        'User-Agent': UserAgent().random,
        'Referer': 'https: // maoyan.com / films?showType = 1',
        'Cookie': '__mta213220267.1587190550292.1587191290179.1587191437295.25;uuid_n_v = v1;uuid = 0A5A1C80813C11EA9D8A655A6973F397430E2D7991094625811C6E62C8F1F2AA;_csrf = fe4e443f547290a9e678d7029aa0e50d5029b40ce1ef416c574eebd099f62bd2;_lxsdk_cuid = 1718bedc8e3c8 - 0697c838e8ca87 - f313f6d - 144000 - 1718bedc8e3c8;_lxsdk = 0A5A1C80813C11EA9D8A655A6973F397430E2D7991094625811C6E62C8F1F2AA;t_lxid = 1718bedc906c8 - 0882ea80061709 - f313f6d - 144000 - 1718bedc906c8 - tid;mojo - uuid = 90cee737830d092ff04977c02db24622;mojo - session - id = {"id": "77e21d528cf76568b4adbd863d5c239d", "time": 1587190550249};_lx_utm = utm_source % 3DBaidu % 26utm_medium % 3Dorganic;Hm_lvt_703e94591e87be68cc8da0da7cbd0be2 = 1587190549, 1587190562, 1587192851;lt = YHtBRCkQkd6X5WhccJyvUtoRiCoAAAAAdwoAABiFKJVgVEUrtEkO1PfmMS_K5dSm1jHGCji - phCfvvml943p1jKv9jCX4l5pt15PuA;lt.sig = kYV1f7VY7TGq545g - celgjPbDHE;mojo - trace - id = 84;Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2 = 1587194427;__mta = 213220267.1587190550292.1587191437295.1587194427679.26;_lxsdk_s = 1718bedc8e4 - 92a - 180 - fba % 7C % 7C124'
    }
    resopen = requests.get(url, headers=header,timeout = 0.5)
    return resopen.text
if __name__ == '__main__':
    n = int(input("请输入你要爬取的页码:"))
    url = 'https://maoyan.com/films?showType=2&offset='
    for i in range(n):
        url = url+str(i*30);
        resp = pa(url)
        analysis_xpath(resp)