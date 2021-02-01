import requests
from bs4 import BeautifulSoup
import os,stat
import urllib.request
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

# res = requests.get('http://tieba.baidu.com/f/index/forumpark?pcn=%E5%B0%8F%E8%AF%B4&pci=161&ct=0&rn=20&pn=1',headers = headers)
# soup = BeautifulSoup(res.text,'html.parser')
# print(soup.prettify())
# results_name = soup.find_all('p','ba_name')
# results_desc = soup.find_all('p','ba_desc')
# for result_name,result_desc in zip(results_name,results_desc):
#     print(result_name.text,result_desc.text)

# for result_name in results_name:
#     print(result_name.text)

##将百度小说吧的 吧名、图片存储到txt
# urls=['http://tieba.baidu.com/f/index/forumpark?cn=&ci=0&pcn=%E5%B0%8F%E8%AF%B4&pci=161&ct=&st=new&pn={}'.format(i) for i in range(31)]
# f = open('F:\百度贴吧名称.txt','w+')
# count = 0
# for url in urls:
#     res = requests.get(url,headers = headers)
#     soup = BeautifulSoup(res.text,'html.parser')
#     result_names = soup.find_all('p','ba_name')
#     result_pics = soup.find_all('img','ba_pic')
#     for result_name,result_pic in zip(result_names,result_pics):
#         count = count + 1
#         f.write(str(count)+'.'+result_name.text+'.'+result_pic.get('src')+'\n')
# print(count)
# f.close()

# 将百度小说吧 贴吧头像保存到本地，图片名称为贴吧名
count1 = 0
count2 = 0
file_path = 'F:\pic'
urls = ['http://tieba.baidu.com/f/index/forumpark?cn=&ci=0&pcn=%E5%B0%8F%E8%AF%B4&pci=161&ct=&st=new&pn={}'.format(i) for i in range(31)]
for url in urls:
    res = requests.get(url,headers = headers)
    soup = BeautifulSoup(res.text,'html.parser')
    result_names = soup.find_all('p','ba_name')
    result_pics = soup.find_all('img','ba_pic')
    print(url)
    for result_name,result_pic in zip(result_names,result_pics):
        count1 = count1 + 1
        if result_pic.get('src') != '':
            count2 = count2 + 1
            # 获取图片后缀
            file_suffix = os.path.splitext(result_pic.get('src'))[1]
            # 拼接图片名称
            filename = '{}{}{}{}'.format(file_path, os.sep, result_name.text, file_suffix)
            # 下载图片，并保存到文件夹
            urllib.request.urlretrieve(result_pic.get('src'),filename=filename)

        # print(file_path)
        # print(os.sep)
        # print(result_name.text)
        # print(result_pic.get('src'))
        # print(file_suffix)
        # print(filename)

