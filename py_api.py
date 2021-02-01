import requests
url = 'https://irpmt.mail.163.com/ir/stat.gif?statId=1_16_191_2399&position=0&ad_oper=show&ad_source=mailad&ad_position=login&uid=m15864763690_1@163.com&domain=email.163.com&rnd=1611651466568'
response = requests.get(url)
print(response.text)