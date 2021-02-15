# 引入包opencv
import cv2

# 下载model文件
# 链接：https://pan.baidu.com/s/1Lo5DU-ttsGWPHqey3g3jtw
# 提取码：1111
# 创建深度神经网络对象cv2.dnn。
# 使用readNetFromTorch()方法，让神经网络加载模型
list = ['candy.t7','composition_vii.t7','feathers.t7','la_muse.t7','mosaic.t7','starry_night.t7','the_scream.t7','the_wave.t7','udnie.t7']
net = cv2.dnn.readNetFromTorch(r"F:\fast_neural_style_models\udnie.t7")
# 设置神经网络后端，使用模型
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
# 读取源图片
img = cv2.imread(r"F:\pic\The Grand Canyon.jpeg")
# 记录源图片的像素行数、像素列数列、通道数（不用获取，用_略过）
row, column, _ = img.shape
# 创建图像的四维连通区域，6个参数（图像、图像比例、图像的空间大小、计算的平均值标量、交换标志、剪裁标志）
blob = cv2.dnn.blobFromImage(img, 1.0, (column, row), (103.939, 116.779, 123.680), swapRB=False, crop=False)
# 创建好的联通对象，交给创建好的神经对象
net.setInput(blob)
# 神经网路分析结果
out = net.forward()
# out不是一个可以用于展示的图像格式，将out转换为图像的三维数组
# cv2.imshow("out",out)
# cv2.error: OpenCV(4.5.1) C:\Users\appveyor\AppData\Local\Temp\1\pip-req-build-0ycehs0d\opencv\modules\core\src\array.cpp:2492: error: (-206:Bad flag (parameter or structure field)) Unrecognized or unsupported array type in function 'cvGetMat'
out = out.reshape(3, out.shape[2], out.shape[3])
out[0] += 103.939
out[1] += 116.779
out[2] += 123.680
out /= 255
out = out.transpose(1, 2, 0)
# 展示输入照片、输出照片
# cv2.imshow("img", img)
cv2.imshow("out", out)
cv2.imwrite(r"F:\pic\udnie.jpeg",out)
cv2.waitKey()
# 释放所有窗口
cv2.destroyAllWindows()
