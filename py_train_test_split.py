# 导入load_iris，加载已有数据
from sklearn.datasets import load_iris
# 导入train_test_split用于打乱、分割样本库
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
# 可视化
import pandas as pd
import mglearn
# k邻近算法
from sklearn.neighbors import KNeighborsClassifier



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

# 利用X_train中数据创建DataFrame
# 利用iris_dataset.feature_names中的字符串（花萼长度、宽度，花瓣长度、宽度）对数据列进行标记
iris_dataframe = pd.DataFrame(X_train,columns=iris_dataset.feature_names)
# 利用DataFrame创建散点图矩阵，按y_train着色
grr = pd.plotting.scatter_matrix(iris_dataframe,c=y_train,figsize=(15,15),marker='o',hist_kwds={'bins':20},s=60,alpha=.8,cmap=mglearn.cm3)
plt.show()

# k邻近算法实例化，设置参数
# knn对象：对算法进行了封装，既包括用训练数据构建模型的算法，也包括对新数据点进行预测的算法，还包括算法从训练数据中提取的信息。
# KNeighborsClassifier类：只保存了训练集
knn = KNeighborsClassifier(n_neighbors=1)
# knn.fit()方法：基于训练集构建模型。
knn.fit(X_train,y_train)

# 使用模型对新数据进行预测。
# 新增一条记录,存放在NumPy数组中，
X_new = np.array([[5,2.9,1,0.2]])
print(X_new)
# knn.predict():预测
predition = knn.predict(X_new)
print("Prediction:{}".format(predition))
print("Predicted target name:{}".format(iris_dataset['target_names'][predition]))


# 使用测试集评估模型
# 方法：由于测试集数据的品种已知，我们有构建模型预测的结果与已知数据对比，计算精度（accuracy品种预测正确占总数据比），来衡量模型的优劣。
y_prediction = knn.predict(X_test)
print("Test set predictions:\n{}".format(y_prediction))
# 使用NumPy.mean()计算精度
print("Test set score:{:.2f}".format(np.mean(y_prediction==y_test)))
# 使用knn.score()计算精度
print("Test set score:{:.2f}".format(knn.score(X_test,y_test)))