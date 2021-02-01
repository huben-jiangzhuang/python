import requests
import re
from bs4 import BeautifulSoup
import time
# 下载斗破苍穹小说
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
# 新建或打开文件，追加可写，指定编码方式utf-8
f = open('d:/doupo.txt','a+',encoding='utf-8')
# 定义函数
def get_info(url):
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.content,'html.parser')
    if res.status_code == 200:
        title = soup.find('div','entry-tit')
        f.write(title.text)
        # print(title.text)
        content = re.findall('<div class="m-post">(.*?)</div>',res.content.decode('utf-8'))[0].replace('<p>','').replace('</p>','\n')
        f.write(content)
        # print(content)
    else:
        pass
# 程序入口
if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(i) for i in range(1,1646)]
    for url in urls:
        get_info(url)
        # time.sleep(1)
f.close()
