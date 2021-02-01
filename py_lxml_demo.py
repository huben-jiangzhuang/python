# 导入lxml中的etree库
from lxml import etree
import requests
# # text变量中存放html代码
# text = '''
# <div>
#     <ul>
#         <li class='red'><h1>red flowsers<h1></li>
#         <li class='yellow'><h2>yellow flowsers<h2></li>
#     </ul>
# </div>
# '''
# # 1.1使用etree.HTML()方法，通过直接读取字符串的方式，将字符串中html解析为Element对象
# html = etree.HTML(text)
# print(html)
# # 1.2输出解析的html代码,并自动修正html
# result = etree.tostring(html)
# print(result)

# 2.1解析html文件。
# 下面语法报错lxml.etree.XMLSyntaxError: Opening and ending tag mismatch: meta line 4 and head, line 6, column 8
# html = etree.parse('flower.html')
# result = etree.tostring(html,pretty_print=True)
# print(result)

# # 2.2自己创建html解析器，增加parser参数
# parser = etree.HTMLParser(encoding='utf-8')
# html = etree.parse('flower.html',parser=parser)
# result = etree.tostring(html,pretty_print=True)
# print(result)

# # 3.使用requets库获取HTML文件，用lxml库解析html文件
# # requests的get方法发出请求，得到响应
# response = requests.get('https://www.baidu.com/').text
# # 使用etree包的HTML方法把html文档解析成element对象
# html = etree.HTML(response)
# # 输出解析过得html文档
# result = etree.tostring(html)
# print(result)


# 4.使用xpath获取糗事百科的某个ID
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
url = 'https://www.qiushibaike.com/text/'
response = requests.get(url,headers=headers)
selector = etree.HTML(response.text)
# 获取某一个ID（可以获取数据）
# ids = selector.xpath('//*[@id="index_header"]/ul/li[2]/a')
# for id in ids:
#     print(id.text)

# 不能获取数据，原因未明
# id = selector.xpath('//*[@id="qiushi_tag_123992807"]/div[1]/a[2]/h2/text()')
# print(id)

# 可以获取数据
# url_infos = selector.xpath('//div[@class="article block untagged mb15 typs_hot"]')
# for url_info in url_infos:
#     id = url_info.xpath('div[1]/a[2]/h2/text()')[0]
#     print(id.strip())

# # 可以获取数据,starts-with
# contents = selector.xpath('//div[starts-with(@class,"article block untagged mb15")]')
# for content in contents:
#     id = content.xpath('div[1]/a[2]/h2/text()')[0]
#     print(id.strip())
# print(len(contents))


# #不能获取数据，contents为空，原因不清楚。 string(.)方法，获取标签套用标签的
# contents = selector.xpath('//div[starts-with(@class,"article block untagged mb15")]')
# for content in contents:
#     c1 = content.xpath('/a[2]/div/div/text()')
#     c2 = c1.xpath('string(.)')
#     print(c2)
# print(len(contents))
