# 1.运行程序，输入密码
# 1）如果字符串是123456，打印”密码正确，登录成功“，程序结束
# 2）如果输入字符串不是123456，打印“密码错误，再次输入”，继续运行程序，直至输入正确

# def log():
#     password = input("请输入密码")
#     if password == '123456':
#         print("密码正确，登录成功")
#     else:
#         print('密码错误，再次输入')
#         log()
# log()


# 2.运行程序，输入密码
# 1）如果字符串是123456，打印”密码正确，登录成功“，程序结束
# 2）如果输入字符串不是123456，打印“密码错误，再次输入”，继续运行程序，
# 3）当密码输入错误第三次后，打印“密码错误超过3次，退出程序”

# i = 0
# while i < 3:
#     password = input("请输入密码")
#     if password == '123456':
#         print("密码正确，登录成功")
#         break
#     else:
#         print('密码错误，再次输入')
#         i = i + 1

# 使用for循环，打印1-10
# for i in range(1,11):
#     print(i)

# 计算1-100的累加和
# i = 1
# sum = 0
# while i <= 100:
#     sum = sum + i
#     i = i +1
# print(sum)

# # list.append(element)：在列表末尾，添加元素
# s = ['how','are','you']
# s.append('fine')
# print(s)
# # ['how', 'are', 'you', 'fine']

# # 截取左闭右开，[m:n)
# s = ['1', '2', '3','4', '5', '6']
# #取一个元素
# print(s[0])
# #取元素区间
# print(s[:2])
# print(s[1:])
# print(s[0:2])
# #间隔一个元素，取值 ['1', '3', '5']
# print(s[0:5:2])
#
# # ['m', 'o', 'n', 'k', 'e', 'y', 'you']

# s = ['1', '2', '1','4', '5', '6'
# sort()降序
# reverse()方法，翻转列表
# s = [1,3,4,45,1,35,3]
# s.reverse()
# print(s)

# 计算元素1出现的次数

# names = ['a','b','c']
# ages = [1,2,3]
# print(zip(names,ages))
# for name,age in zip(names,ages):
#     print(name,age)

# urls = ['https://www.baidu.com/#ie=UTF-8&wd={}'.format(number) for number in range(1,14)]
# for url in urls:
#     print(url)

# user_info = {
#     'name':'a',
#     'age':'1',
#     'sex':'man'
# }
# print(user_info)
# 覆盖写入
# f = open('d:/1.txt','r')
# content = f.read()
# print(content)
# f.close()

class Person:
    name = "人类"
    def change(self):
        print('改变')
    def __init__(self):
        print('实例化后，自动执行')
p = Person()
class Teacher(Person):
    name = '老师'
t = Teacher()
print(p.name,t.name)