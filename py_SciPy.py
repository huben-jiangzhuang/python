# SciPy是Python用于科学计算得函数集合
# 功能：线性代数高级程序、数学函数优化、信号处理、特殊数学函数、统计分布
# scikit-learn利用SciPy中的函数集合来实现算法,数据的另一种表达方式是稀疏矩阵scipy.sparse。
from scipy import sparse
import numpy as np
# 创建一个NumPy4*4的二维数组，对角线为1，其余都是0
eye = np.eye(4)
print("NumPy array:\n{}".format(eye))
# 将NumPy数组转换为CSR格式的SciPy稀疏矩阵，只保存非零元素
sparse_matrix =sparse.csr_matrix(eye)
print("\nSciPy sparse CSR matrix:\n{}".format(sparse_matrix))
# 创建COO稀疏矩阵
data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data,(row_indices,col_indices)))
print("COO representation:\n{}".format(eye_coo))