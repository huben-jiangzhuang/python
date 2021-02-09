# 提取文本中关键字，python第三方库jieba
import jieba.analyse
# 要解析的文本
path = 'F://cs.txt'
fp = open(path,'r',encoding='utf-8')
content = fp.read()
try:
    tags = jieba.analyse.extract_tags(content,topK=100,withWeight=True)
    for item in tags:
        print(item[0])
finally:
    fp.close()