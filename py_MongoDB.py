import pymongo
# 连接到数据库
client = pymongo.MongoClient('127.0.0.1',27017)
# 新建mydb数据库
mydb = client['mydb']
# 新建test数据集合
test = mydb['test']
# 以上代码，先保证MongoDB服务已经启动并连接。
# 此时，win+R——cmd，输入mongo连接到数据库，输入show databases没有显示新建的数据库。因为MongoDB需要插入数据后，才可以建立数据库。
# 插入数据
test.insert_one({'name':'Hana','sex':'男','grade':89})