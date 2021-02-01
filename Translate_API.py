# 失败了
import requests
import json
word = input("请输入中文")
'https://wonapi.maxleap.cn/1.0/products/client/2187'
url = 'http://howtospeak.org:443/api/e2c?user_key=dfcacb6404295f9ed9e430f67b641a8e&notrans=0&text={}'.format(word)
response = requests.get(url)
json_data = json.loads(response.text)
english_word = json_data['english']
print(english_word)