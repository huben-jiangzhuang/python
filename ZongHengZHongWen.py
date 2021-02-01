# 爬取纵横中文网所有小说列表
# http://book.zongheng.com/store.html
# http://book.zongheng.com/store/c0/c0/b0/u0/p2/v9/s9/t0/u0/i1/ALL.html
# http://book.zongheng.com/store/c0/c0/b0/u0/p3/v9/s9/t0/u0/i1/ALL.html
# 'http://book.zongheng.com/store/c0/c0/b0/u0/p{str(i)}/v9/s9/t0/u0/i1/ALL.html'.format(i) for i in range(1,1000)
# 导入包
import requests
from lxml import etree
import xlwt

# 网址
urls = ['http://book.zongheng.com/store/c0/c0/b0/u0/p{}/v9/s9/t0/u0/i1/ALL.html'.format(str(i)) for i in range(1,2)]
# 爬取数据【小说名、作者ID、小说类型、完成情况、摘要、字数】
all_info_list = []
for url in urls:
    # 获取响应
    html = requests.get(url)
    # 解析响应
    selector = etree.HTML(html.text)
    # 获取一本小说的所有内容，以此为大标签循环
    infos = selector.xpath('//div[@class="bookinfo"]')
    for info in infos:
        # 小说名称
        name = info.xpath('div[1]/a/text()')[0]
        # 作者
        author = info.xpath('div[2]/a[1]/text()')[0]
        # 类型
        type = info.xpath('div[2]/a[2]/text()')[0]
        # 完成情况
        state = info.xpath('div[2]/span[1]/text()')[0].strip()
        # 更新时间
        update_time = info.xpath('div[2]/span[2]/text()')[0].strip()
        # 摘要
        introduce = info.xpath('div[3]/text()')[0]
        # 最新章节
        last_title = info.xpath('div[4]/a/text()')[0]
        # 每一本书的信息作为元组，存放到一个列表中
        info_list = [name,author,type,state,update_time,introduce,last_title]
        # 每一本书作为元组，存放到列表中
        all_info_list.append(info_list)
for list in all_info_list:
    print(list)




