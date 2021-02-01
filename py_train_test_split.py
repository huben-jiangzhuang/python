# 导入load_iris，加载已有数据
from sklearn.datasets import load_iris
# 导入train_test_split用于打乱、分割样本库
from sklearn.model_selection import train_test_split

# 加载数据
iris_dataset = load_iris()
# train_test_split()函数原理
# 1.利用伪随机数生产器将数据集打乱
# 2.为了确保多次运行同一函数能够得到相同的输出，利用random_state参数指定了随机数生成器的种种。
# 3.输出结果：X_train,X_test,y_train,y_test都是NumPy数组
X_train,X_test,y_train,y_test = train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)
# 查看X_train:训练数据 的数量
print("X_train shape:{}".format(X_train.shape))
# 查看y_train:训练数据标签 的数量
print("y_train shape:{}".format(y_train.shape))
# 查看X_test:测试数据 的数量
print("X_test shape:{}".format(X_test.shape))
# 查看y_test:测试数据标签 的数量
print("y_test shape:{}".format(y_test.shape))

