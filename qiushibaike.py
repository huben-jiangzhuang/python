import requests
from bs4 import BeautifulSoup
import re

# 获取糗事百科笑话内容

# headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
info_lists = []
def judgement_sex(class_name):
    if class_name == 'manIcon':
        return '男'
    else:
        return '女'
def get_info(url):
    res = requests.get(url)
    ids = re.findall('<h2>(.*?)</h2>',res.text,re.S)
    sexs = re.findall('<div class="articleGender (.*?)">',res.text,re.S)
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>',res.text,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
    laughts = re.findall('<span class="stats-vote"><i class="number">(\d+)</i> 好笑',res.text,re.S)
    comments = re.findall('<span class="stats-comments">.*?<i class="number">(\d+)</i> 评论',res.text,re.S)

    # for id,sex,level,laught,comment in zip(ids,sexs,levels,laughts,comments):
    #     print(id.strip(),judgement_sex(sex),level,laught,comment)


    # print(len(ids),len(sexs),len(levels),len(contents),len(laughts),len(comments))

    # for id in ids:
    #     print(id.strip())
    # for sex in sexs:
    #     print(judgement_sex(sex))
    # for level in levels:
    #     print(level)
    # for content in contents:
    #     print(content)
    # for laught in laughts:
    #     print(laught)
    # for comment in comments:
    #     print(comment)

    for id,sex,level,content,laught,comment in zip(ids,sexs,levels,contents,laughts,comments):
        info = {
            'id':id.strip(),
            'sex':judgement_sex(sex),
            'level':level,
            'content':content.replace('<br/>','\n').strip(),
            'laught':laught,
            'comment':comment
        }
        info_lists.append(info)
if __name__ == '__main__':
    f = open('d:/qsbk.txt','a+',encoding='utf-8')
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(i) for i in range(1,14)]
    for url in urls:
        get_info(url)
    for info_list in info_lists:
         try:
            f.write('用户ID：'+info_list['id']+'  ')
            f.write('用户性别：'+info_list['sex'] + '  ')
            f.write('用户等级：'+info_list['level'] + '\n')
            f.write(info_list['content'] + '\n')
            f.write('好笑数：'+info_list['laught'] + '  ')
            f.write('评论数：'+info_list['comment'] + '\n\n')
         except UnicodeError:
            pass




