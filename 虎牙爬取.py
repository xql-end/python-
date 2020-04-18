from selenium import webdriver
from lxml import etree
from time import sleep
#跳过浏览器
options = webdriver.ChromeOptions()
options.add_argument('--headless')
chrome = webdriver.Chrome(options=options)#模拟谷歌浏览器
url = 'https://www.huya.com/g/lol'
chrome.get(url)
z = 1
while True:
    print("正在打印第"+str(z)+"页------------------------------------------------------------")
    z += 1
    sleep(5)#不要让程序太快
    html = chrome.page_source
    e = etree.HTML(html)
    names = e.xpath('//i[@class="nick"]/text()')#获取主播名
    counts = e.xpath('//i[@class="js-num"]/text()')#获取主播人气
    for i,j in zip(names,counts):
        print(i+":"+j)
    if chrome.page_source.find('laypage_next')!=-1:#判断是否有下一页
        chrome.find_element_by_xpath('//a[@class="laypage_next"]').click()#点击下一页
    else:
        break;