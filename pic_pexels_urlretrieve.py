# 失败
# 导入库文件
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
# 初始化list，存入图片
list = []
# 要爬取图片网址
url = 'https://www.pexels.com/zh-cn/'
# 加入请求头，用于伪装成浏览器，便于爬虫稳定性
headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,'lxml')
imgs = soup.select('article > a > img')
for img in imgs:
    photo = img.get('src')
    list.append(photo)
# 定义图片存放文件夹
path = 'd://pic1/'
for item in list:
    data = requests.get(item,headers=headers)
    fp = open(path+item.split('?')[0][-10:],'wb')
    fp.write(data.content)
    fp.close()