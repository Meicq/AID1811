# 打印输出以下内容:
# 12345
# 23456
# 34567
# 45678
# 56789
n = 0
i = 1
j = 1
a = 1
while i <= 5:
    while j <= 5:
        n = n * 10 + a
        a += 1
        j += 1
    print(n)
    i += 1
    a = i
    n = 0
    j = 1




# # 打印输出以下内容:
# # 12345
# # 23456
# # 34567
# # 45678
# # 56789
# # 打印5行
# import time
# x = 1
# while x <= 5:
#     # 打印一行数字
#     y = x
#     while y <= x + 4:
#         time.sleep(1)
#         print(y,end='',flush=True) # 打印输出不换行
#         y += 1
#     print() # 一行结束了,打印换行
#     x += 1  
