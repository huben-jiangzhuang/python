# 将豆瓣读书前250条记录下载到csv中
# 导入包
from lxml import etree
import requests
import csv
# 创建csv
fp = open('d:\\douban.csv','wt',newline='',encoding='utf-8')
writer = csv.writer(fp)
# 往csv中插入表头
writer.writerow(('name','url','author','publisher','date','price','rate','comment'))
# 构造url
urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
# 头文件
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
# 使用xpath抓取数据
for url in urls:
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    # 选取所有的tr标签，并且属性为class='item'
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        # 书名
        name = info.xpath('td/div/a/@title')[0]
        # 书，超链接
        url = info.xpath('td/div/a/@href')[0]
        # 作者、出版社、出版日期、价格等信息
        book_infos = info.xpath('td/p/text()')[0].split('/')
        # 作者，只去第一作者
        author = book_infos[0]
        # 出版社
        publisher = book_infos[-3]
        # 出版日期
        date = book_infos[-2]
        # 价格
        price = book_infos[-1]
        # 评分
        rate = info.xpath('td/div/span[@class="rating_nums"]/text()')[0]
        # 评论
        comments = info.xpath('td/p/span[@class="inq"]/text()')
        if len(comments)==0:
            comment = ''
        else:
            comment = comments[0]
        writer.writerow((name,url,author,publisher,date,price,rate,comment))
# 关闭文件
fp.close()