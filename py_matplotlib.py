# matplotlib是绘图库
# 功能：生产可发布的、可视化内容，如折线图、直方图、散点图
import matplotlib.pyplot as plt
import numpy as np
# 在-10和10之间生成一个数列，共100个数
x = np.linspace(-10,10,100)
# 用正弦函数创建第二个数组
y = np.sin(x)
# plot函数绘制一个数组关于另一个数组的折线图
plt.plot(x,y,marker="x")
plt.show()