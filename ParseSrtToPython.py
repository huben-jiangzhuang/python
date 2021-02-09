# srt字幕
import srt
# sqlite3数据库
import sqlite3
# 读取srt文件
f = open('f:\supernaturals1e1.srt','r+',encoding='utf-8')
# 将srt文件解析为python,存储到list
subtitle_generator = srt.parse(f)
subtitles = list(subtitle_generator)

# 新建、连接数据库srt.db
conn = sqlite3.connect('F:\srt.db')
# 新建表:srt
# 新建列:name,starttime、endtime、chinese、english
c = conn.cursor()
# c.execute('''
# create table srt
# (
# name char(50),
# starttime date,
# endtime date,
# chinese text,
# english text
# );
# ''')
# # 插入数据
# sql = "insert into srt (name,starttime,endtime,chinese,english)  values('supernaturals1e1','0:01:53.330000','0:01:57.330000','{\pos(235.108,242)}最新连载海外影视剧下载','请登陆 www.YYeTs.com')"
# c.execute(sql)
# cursor = c.execute('select * from srt')
# for row in cursor:
#     print(row[1])
# # 提交
# conn.commit()
# # 关闭
# conn.close()
for subtitle in subtitles:
    try:
        contents = subtitle.content.split('\n')
        ch = contents[0]
        en = contents[1]
        if ch is None:
            ch = ''
        else:
            # 处理字符串中的转移字符
            ch = conn.escape(ch)
        if en is None:
            en = ''
        else:
            en = conn.escape(en)
        start = subtitle.start
        end = subtitle.end
        # print("insert into srt (name,starttime,endtime,chinese,english)  values('supernaturals1e1','{}','{}','{}','{}') ".format(start,end,ch,en))
        # 双引号用在外面，单引号用在里面，报错sqlite3.OperationalError: near "s": syntax error。（可能原因，插入值里面存在单引号）
        # sql = "insert into srt (name,starttime,endtime,chinese,english)  values('supernaturals1e1','{}','{}','{}','{}') ".format(start,end,ch,en)
        # 单引号在外，双引号在内，报错sqlite3.OperationalError: near "别怕黑": syntax error（原因，插入值里面有双引号）
        # 解决方案，把参数里面引号前加斜杠，转移
        sql ='insert into srt (name,starttime,endtime,chinese,english)  values("supernaturals1e1","{}","{}","{}","{}")'.format(start,end,ch,en)
        c.execute(sql)
    except IndexError:
        print()
conn.close()


