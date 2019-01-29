# # 打印输出编码从1~10000之间的所有的字符
# i = 1
# while i <= 60000:
#     print(chr(i),end=' ')
#     i += 1




# 6.随机生成6位数字验证码
import random
i = 1
while i <= 6:
    print(random.randint(0,9),end='')
    i += 1
# 相当于上面while循环输出代码
# print(random.randint(0,9))
# print(random.randint(0,9))
# print(random.randint(0,9))
# print(random.randint(0,9))
# print(random.randint(0,9))
# print(random.randint(0,9))
