# 输入一个数字,求阶乘？
n = int(input('请输入数字:'))
i = 1   # 循环条件的初始化
jiecheng = 1    # 定一变量,保存阶乘
while i <= n:
    jiecheng = jiecheng * i     # 求阶乘
    i = i + 1
print(n,'的阶乘=',jiecheng)
