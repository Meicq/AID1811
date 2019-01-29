# 闰年判断程序
year = int(input('请输入年份:'))
# 实现3个条件
a = year % 4 == 0
b = year % 100 != 0
c = year % 400 == 0
# 3个条件的逻辑判断
res = a and b or c
# 打印输出结果
print(res)