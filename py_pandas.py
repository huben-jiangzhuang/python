# pandas用于处理和分析数据
# 功能：pandas DataFrame是一张表格，每一列的数据类型可以互不相同，可以像sql一样查询和连接，也可以从不同文件格式、数据库中提取数据
import pandas as pd
from IPython.display import display
# 利用字典，创建关于人的简单数据集
data = {
    'name':["a","b","c"],
    'location':["x","y","z"],
    'age':[1,2,3]
}
#利用字典，创建DataFrame
data_pandas = pd.DataFrame(data)
# 利用IPython.display打印DataFrame
display(data_pandas)
# print(data_pandas)
# 查询表格，查询age>1的记录
print(data_pandas[data_pandas.age>1])