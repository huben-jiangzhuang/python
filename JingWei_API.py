# 失败了
import requests
# url = 'https://jisuapigeoconvert.api.bdymkt.com/geoconvert/coord2addr'
# par = {'lat':'30.2812129803','lng':'120.11523398'}
# response = requests.get(url,par)
# print(response.text)
import json
import pprint
address = input('请输入地点：')
par = {'address':address,'key':'cb649a25clf81c1451adbeca73623251'}
url = 'http://restapi.amap.com/v3/geocode/geo'
response = requests.get(url,par)
json_data = json.loads(response.text)
pprint.pprint(json_data)