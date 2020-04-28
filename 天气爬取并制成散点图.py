from matplotlib import pyplot as plt
from matplotlib import font_manager
font = font_manager.FontProperties(fname='C:/WINDOWS/FONTS/MSYH.TTC')
import requests
from lxml import etree
from fake_useragent import UserAgent
"""或取3月和10月的气温"""
headers = {
    'User-Agent':UserAgent().random
}
y_3 = []
y_10 = []
data_3=[]
data_10=[]
urls = ['https://weather.mipang.com/tianqi-2606/3yuefen.html','https://weather.mipang.com/tianqi-2606/10yuefen.html']
for url in range(2):
    respone = requests.get(urls[url],headers=headers)
    e = etree.HTML(respone.text)
    date = e.xpath('//div[@class="tb"]//td[1]/text()')
    max_t = e.xpath('//div[@class="tb"]//td[2]/text()')
    min_t = e.xpath('//div[@class="tb"]//td[3]/text()')
    weather = e.xpath('//div[@class="tb"]//td[4]/text()')
    print(max_t)
    if url == 0:
        for max_ts,min_ts,dates in zip(max_t,min_t,date):
            t = int((int(max_ts)+int(min_ts))/2)
            y_3.append(t)
            data_3.append(dates)
    else:
        for max_ts,min_ts,dates in zip(max_t,min_t,date):
            t =int((int(max_ts)+int(min_ts))/2)
            y_10.append(t)
            data_10.append(dates)
"""绘制散点图"""
x_3 = range(1,32)
x_10 = range(51,82)
plt.figure(figsize=(20,8),dpi=100)
plt.scatter(x_3,y_3,label='3月气温')
plt.scatter(x_10,y_10,label='10月气温')
x =list( x_10)+list(x_3)
y = data_3+data_10
print(y)
plt.xticks(x[::3],y[::3],rotation=30)
plt.ylabel('平均气温',fontproperties = font)
plt.ylabel('时间',fontproperties = font)
plt.title('3月和10月的气温散点图',fontproperties = font)
plt.legend(prop=font)
plt.show()
