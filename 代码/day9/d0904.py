# 函数方法求斐波那契数列
# f(n) = f(n-1) + f(n-2),f(0)=0,f(1)=1
def fbnq(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fbnq(n-1) + fbnq(n-2)
print(fbnq(20))



# # 函数方法求阶乘
# # f(n) = n * f(n-1),f(1) = 1
# def jiecheng(n):
#     if n == 1:
#         return 1
#     return n*jiecheng(n-1)
# print(jiecheng(6))


# # 递归思想
# i = 0
# def fun():
#     print('函数被调用了...')
#     global i
#     i += 1
#     print(i)
#     fun()
# fun()