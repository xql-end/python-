from threading import Thread
from queue import Queue
import requests
from fake_useragent import UserAgent
from lxml import etree
#创建爬虫类
class reptile(Thread):
    def __init__(self,url,html_info):
        Thread.__init__(self)
        self.url = url
        self.html_info = html_info
    def run(self):
        headers = {
            'User-Agent' : UserAgent().random
        }
        while(self.url.empty()==False):
            respon = requests.get(self.url.get(),headers=headers)
            if respon.status_code==200:#判断状态
                self.html_info.put(respon.text)

#创建解析和保存类
class analysis(Thread):
    def __init__(self,html_info):
        Thread.__init__(self)
        self.html_info = html_info
    def run(self):
        while (self.html_info.empty()==False) :
            e = etree.HTML(self.html_info.get())
            cont = e.xpath('//h4/a/text()')#用xpath解析小说的名字
            with open('小说名.txt','a',encoding='utf-8') as f:
                for i in cont:
                    f.write(i+"\n")#存储


if __name__ == '__main__':
    #存储url的容器
    url = Queue()
    #存储内容的容器
    html_info = Queue()
    base_url = 'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page={}'
    for i in range(1,20):
        new_url = base_url.format(i)
        url.put(new_url)
        #new一个线乘
        clist =[]
    for i in range(1,4):
        c = reptile(url,html_info)
        clist.append(c)
        c.start()
    for c in clist:
        c.join()#让线程等待
    cot = analysis(html_info)
    cot.start()