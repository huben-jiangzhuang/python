import re
import requests
from bs4 import BeautifulSoup

# re正则表达式练习

# a = 'xxffdgehehkhpoiqwegnxx'
# infos = re.findall('xx(.*?)xx',a)
# print(infos)



#
# # re.search(pattern,string,flags=0)
# # pattern正则表达式
# # string要匹配的字符串
# # flags正则表达式的匹配方式，是否区分大小写、多行匹配等
# a = 'one1two2three3'
# infos1 = re.search('\d+',a)
# # 打印出，匹配到的第一个符合规律的内容
# print(infos1.group())
#
#
# # re.sub(pattern,repl,string,count=0,flags=0)
# # pattern:匹配的正则表达式
# # repl:替换字符串
# # string：原始字符串
# # counts:匹配后替换的最大次数，默认0替换所有匹配
# # 例如：电话号码123-4567-1234，把-去掉
# phone = '123-4567-1234'
# new_phone = re.sub('\D*','',phone)
# print(new_phone)
#
#
# a = 'one1two2three3'
# infos2 = re.findall('\d+',a)
# print(infos2)


# # 获取淘宝某页面所有价格信息
# url = 'https://list.tmall.com/search_product.htm?q=%D3%F0%C8%DE%B7%FE%C5%AE&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton'
# res = requests.get(url)
# prices = re.findall('<em title="(.*?)">',res.text)
# for p in prices:
#     print(p)

a = '<div>指'\
    '数</div>'
word = re.findall('<div>(.*?)</div>',a)
print(word)
