# 奇数判断程序
# 1.接收键盘输入的数字
num = input('请输入数字:')
# 字符串转数字
num = int(num)
# 判断是否是奇数
res = num % 2 == 1
# 打印输出结果
print(res)