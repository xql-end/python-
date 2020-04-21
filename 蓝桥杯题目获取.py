import requests
from fake_useragent import UserAgent
from jsonpath import jsonpath
from lxml import etree
headers = {'User-Agent':UserAgent().chrome,
           'Cookie': 'gr_user_id=22ebbf32-78b6-47be-a0ee-6a20e210e55c; JSE=USRd4RnTLA; Hm_lvt_2cb9ea119abc27f41b5e226ccca7d271=1582800677,1583141910; JSESSIONID=7E72F6F00E5BC74C4B349C7FB14439FA; _SESSIONKEY=MH6A2AHV478VVCIY3T3H; lqtoken=F55379CF6C1F16E14B15534DFA7AC99E'
           }
def huoqu(url,data):
    respone = requests.post(url, headers=headers, data=data)
    # respone.encoding = respone.raise_for_status()
    names = jsonpath(respone.json(), '$..fcontent')#获取内容
    title = jsonpath(respone.json(), '$..title')#获取题目
    e = etree.HTML(names[0])
    name = e.xpath('//div')
    for i in name:
        ff = i.xpath('string(.)')
        with open('蓝桥杯题目/'+title[0]+'.txt','a',encoding='utf-8') as f:
            f.write(ff+"\n")#保存文件
if __name__ == '__main__':
    a = int(input("获取的题数:"))
    url = 'http://lx.lanqiao.cn/problem.Problem.dt'
    for i in range(1,a):
        gpid = 'T'+str(i)
        data = {
            'cmd': 'description',
            'gpid': gpid
        }
        huoqu(url,data)