# 爬取纵横中文网所有小说列表、图片
# http://book.zongheng.com/store.html
# http://book.zongheng.com/store/c0/c0/b0/u0/p2/v9/s9/t0/u0/i1/ALL.html
# http://book.zongheng.com/store/c0/c0/b0/u0/p3/v9/s9/t0/u0/i1/ALL.html
# 'http://book.zongheng.com/store/c0/c0/b0/u0/p{str(i)}/v9/s9/t0/u0/i1/ALL.html'.format(i) for i in range(1,1000)
# 导入包
import requests
from lxml import etree
import xlwt
import os
import urllib.request

# 初始化列表，存储数据
all_info_list = []
# 定义函数，爬取数据【小说名、作者ID、小说类型、完成情况、摘要、字数】
def get_info(url):
    # 获取响应
    html = requests.get(url)
    # 解析响应
    selector = etree.HTML(html.text)

#     图片(文件)下载, 核心方法是urllib.urlrequest模块的urlretrieve()方法
#     导入包import urllib.request
#     urlretrieve(url, filename=None, reporthook=None, data=None)
#     url: 文件url
#     filename: 保存到本地时, 使用的文件(路径)名称
#     reporthook: 文件传输时的回调函数
#     data: post提交到服务器的数据
# 该方法返回一个二元元组("本地文件路径", < http.client.HTTPMessage对象 >)
    # 获取照片
    # infos_pic_src = selector.xpath('//div[@class="bookimg"]/a/img[@src]')
    # infos_pic_name = selector.xpath('//div[@class="bookimg"]/a/img[@alt]')
    infos_pic = selector.xpath('//div[@class="bookimg"]')
    for pic in infos_pic:
        pic_name = pic.xpath('a/img/@alt')[0]
        pic_src = pic.xpath('a/img/@src')[0]
        # print(pic_name)
        # print(pic_src)
        name = 'd://pic//'+pic_name+'.'+pic_src.split('.')[-1]
        # print(name)
        urllib.request.urlretrieve(pic_src,name)
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
# 主程序入口
if __name__ == '__main__':
    # 网址
    urls = ['http://book.zongheng.com/store/c0/c0/b0/u0/p{}/v9/s9/t0/u0/i1/ALL.html'.format(str(i)) for i in range(1,5)]
    # 爬取数据
    for url in urls:
        get_info(url)
    # 定义Excel表头
    header = ['小说名称','小说作者','小说类型','完成状况','更新时间','简介','最新章节']
    # 创建工作簿
    book = xlwt.Workbook(encoding='utf-8')
    # 创建工作表
    sheet = book.add_sheet('sheet1')
    # 遍历列表，写入表头
    for h in range(len(header)):
        # 第1行，第h+1列写入
        sheet.write(0,h,header[h])
    # 遍历写入爬虫数据
    # 从第2行开始写入
    i = 1
    # 遍历每一本小说
    for list in all_info_list:
        # 从第1列开始写入
        j = 0
        # 遍历每一本小说中的每个字段信息
        for data in list:
            sheet.write(i,j,data)
            # print(data)
            # 下一列
            j = j + 1
        # 下一行
        i = i + 1
    book.save('d://xiaoshuo.xls')