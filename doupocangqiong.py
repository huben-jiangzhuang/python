import requests
import re
import time
from bs4 import BeautifulSoup
# 下载斗破苍穹小说
f = open('F:\dp.txt','a+',encoding='utf-8')
urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(i) for i in range(1,1646)]
url = 'http://www.doupoxs.com/doupocangqiong/1.html'
for url in urls:
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html.parser')
    # 获取标题
    h = soup.find('div','entry-tit')
    # f.write(h.text)
    print(h.text)
    # 获取正文
    t = re.findall('<div class="m-post">(.*?)</div>',res.content.decode('utf-8'))[0].replace('<p>','').replace('</p>','\n')
    # f.write(t)
    print(t)
f.close()
