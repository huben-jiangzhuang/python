import requests
from bs4 import BeautifulSoup
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
res = requests.get('https://sz.xiaozhu.com/search-duanzufang-p2-0/',headers = headers)
# print(res)
# print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
# print(soup.prettify())
# result = soup.find('div',attrs='btn_pink_search')
results = soup.select('#page_list > ul > li:nth-child(22) > div.result_btm_con.lodgeunitname > div:nth-child(1) > span > i')
print(results)

