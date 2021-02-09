# 爬取豆瓣音乐top250条
#导入库
import requests
from lxml import etree
import re
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
# 获取详细信息
def get_music_info(url):
    # 返回响应
    response = requests.get(url,headers=headers)
    # 格式化
    selector = etree.HTML(response.text)
    # 获取每首音乐的所有信息
    # music_infos = selector.xpath('//div[@class="p12"]')
    # '//*[@id="content"]/div/div[1]/div/table[7]/tbody/tr/td[2]/div'
    # # 选取所有的tr标签，并且属性为class='item'
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
         name = info.xpath('a/text()')
         text = info.xpath('p/text()')
         print(name+'\n'+text)

# 主程序入库
if __name__=='__main__':
    urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
    for url in urls:
        get_music_info(url)

