# 鸢尾花（Iris）数据集，在scikit-learn的datasets模块中，可以调用load_iris函数加载数据
from sklearn.datasets import load_iris
# load_iris函数返回的Bunch对象,类似字典，里面是键值对
# return Bunch(data=data,
#              target=target,
#              frame=frame,
#              target_names=target_names,
#              DESCR=fdescr,
#              feature_names=feature_names,
#              filename=iris_csv_filename)
iris_dataset = load_iris()
# 查看键
print("keys of iris_dataset:\n{}".format(iris_dataset.keys()))
# 查看DESCR键，对应的值（是数据集的简要说明）
print(iris_dataset['DESCR'][:200]+"\n")
# target_names键对应的值是：要预测花的品种
print("Target names:{}".format(iris_dataset['target_names']))
# feature_names对应的值：对每个特征进行说明，花萼长度、宽度，花瓣长度、宽度
print("feature names:\n{}".format(iris_dataset['feature_names']))
# data是NumPy数组，存放测量过得花朵，每一行对应一朵花，列代表feature_names四个测量数据
# data存放在NumPy数组中
print("type of data:{}".format(type(iris_dataset['data'])))
# 查看前5个样本的特征数据（每一行叫样本，每一列叫特征）
print("first five rows of data:\n{}".format(iris_dataset['data'][:5]))
# 查看库中，样本数量、特征数量（查看行数、列数）
print("shape of data:{}".format(iris_dataset['data'].shape))
# target数组存放测量过花朵的品种，是NumPy数组
print("type of target:{}".format(type(iris_dataset['target'])))
# target是一维数组，每一行是一朵花，查看行数
print("shape of target:{}".format(iris_dataset['target'].shape))
#target查看样本中所有品种，品种用0-2数字代替，0代表setosa,1代表versicolor,2代表virginica
print("target:\n{}".format(iris_dataset['target']))