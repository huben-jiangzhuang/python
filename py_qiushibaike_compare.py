import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
import time
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,14)]
# 文件路径最好用两道杠，避免报错OSError: [Errno 22] Invalid argument: 'D:\re.txt'
f1 = open('D:\\re.txt','a+',encoding='utf-8')
f2 = open('d:\\bs.txt','a+',encoding='utf-8')
f3 = open('d:\\lxml.txt','a+',encoding='utf-8')
info_list_re = []
info_list_bs = []
info_list_lxml = []
# 使用正则爬虫
def re_scraper(url):
    # response结果要decode('utf-8'),否则报错
    # return _compile(pattern, flags).findall(string)
    # TypeError: cannot use a string pattern on a bytes - like
    response = requests.get(url,headers=headers).content.decode('utf-8')
    ids = re.findall('<h2>(.*?)</h2>',response,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',response,re.S)
    laughts = re.findall('<span class="stats-vote">.*?<i class="number">(\d+)</i>',response,re.S)
    comments = re.findall('<span class="stats-comments">.*?<i class="number">(\d+)</i>',response,re.S)
    for id,content,laught,comment in zip(ids,contents,laughts,comments):
        info = {
            'id':id,
            'content':content,
            'laught':laught,
            'comment':comment
        }
        info_list_re.append(info)
        # print(id,content,laught,comment)
        # f1.write(id+content+laught+comment)
        return info   #只返回，不保存数据
# BeautifulSoup爬虫
def bs_scraper(url):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,'lxml')
    ids = soup.select('a > h2')
    contents = soup.select('a.contentHerf > div > span')
    laughts = soup.select('div.stats > span.stats-vote > i')
    comments = soup.select('div.stats > span.stats-comments > a > i')
    for id,content,laught,comment in zip(ids,contents,laughts,comments):
        info = {
            'id':id,
            'content':content,
            'laught':laught,
            'comment':comment
        }
        info_list_bs.append(info)
        # print(id.text.strip(),content.text.strip(),laught.text,comment.text)
        # f2.write(id.text.strip()+content.text.strip()+laught.text+comment.text)
        return info

# lxml爬虫
def lxml_scraper(url):
    response = requests.get(url,headers=headers).content
    selector = etree.HTML(response)
    url_infos = selector.xpath('//div[starts-with(@class,"article block untagged mb15")]')
    try:
        for url_info in url_infos:
            id = url_info.xpath('div[1]/a[2]/h2/text()')[0]
            content = url_info.xpath('a[1]/div/span/text()')[0]
            laught = url_info.xpath('div[2]/span[1]/i/text()')[0]
            comment = url_info.xpath('div[2]/span[2]/a/i/text()')[0]
            info = {
                'id': id,
                'content': content,
                'laught': laught,
                'comment': comment
            }
            info_list_lxml.append(info)
            return info
            # print(id, content, laught, comment)
            # f3.write(id+content+laught+comment)
    # pass掉索引超界问题
    except IndexError:
        pass
# 主程序入口
if __name__ == '__main__':
    # 循环3中方法,
    # 参数name，表示爬虫类型
    # 参数scraper,表示爬虫方法
    for name,scraper in [('Regular expressions',re_scraper),('BeautifulSoup',bs_scraper),('Lxml',lxml_scraper)]:
        # 开始计时
        start = time.time()
        # 每一种爬虫方法都遍历13页
        for url in urls:
            scraper(url)
        # 计时结束
        end = time.time()
        # 打印爬虫类型，已经对应类型的结束时间减去开始时间（即 运行时间）
        print(name,end-start)
    print(str(len(info_list_re))+'\n'+str(len(info_list_bs))+'\n'+str(len(info_list_lxml)))
    f1.close()
    f2.close()
    f3.close()