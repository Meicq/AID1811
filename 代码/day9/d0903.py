# 计算100以内的质数和
# 使用函数的方法计算100以内的质数和
def iszhishu(n): # 定义函数,判断一个数字是不是质数
    for x in range(2,n): # 获取从2~(n-1)之间的元素
        if n % x == 0: # 如果n对x整除
            return False # 返回不是质数的结果
    return True # 都不能整除,那么就是质数，返回结果

he = 0
for y in range(2,100): # 获取从2~100之间的数据
    if iszhishu(y): # 如果y是质数
        he += y # 累加求和
print(he)



# 获取每一个质数
# he = 0
# i = 2
# while i <= 100:
#     j = 2
#     while j < i:
#         if i % j == 0:
#             # print(i,'不是质数')
#             break
#         j += 1
#     else:
#         he += i
#     i += 1
# print(he)

