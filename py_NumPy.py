# NumPy是Python科学计算的基础包
# 功能：多维数组、高等数学函数（线性代数、傅里叶变换）、伪随机数生成器
# NumPy核心功能：ndarray类，即多维数组。（多维数组的所有元素必须是同一类型）
# scikit-learn用到的所有数据必须转成NumPy数组。
import numpy as np
x = np.array([[1,2,3],[4,5,6]])
print("x:\n{}".format(x))
