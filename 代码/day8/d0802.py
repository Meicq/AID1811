# 自定义一个函数判断数字是否是奇数
# 函数定义
def isjishu(num):# num是形参,定义时候的参数就是形参
    if num % 2 == 1:
        # print(num,'是奇数')
        return True
    else:
        # print(num,'是偶数')
        return False
# 函数调用
res = isjishu(10)
if res:
    print('是奇数')
else:
    print('不是奇数')

print(isjishu(10)) # 10是实参,程序运行时实际传递的参数
print(isjishu(9)) # 9是实参,程序运行时实际传递的参数
#isjishu() # 报错:TypeError: isjishu() missing 1 required positional argument: 'num',程序运行时没有提供实际传递的参数





# # 函数定义
# def isjishu():
#     num = int(input('请输入数字：'))
#     if num % 2 == 1:
#         print(num,'是奇数')
#     else:
#         print(num,'是偶数')
# # 函数调用
# isjishu()
# isjishu()


# # 自定义判断100以内的质数的函数
# def zhishu():
#     i = 1
#     while i <= 100:
#         if i == 1:
#             print(i,'既不是质数，也不是合数')
#         else:
#             j = 2
#             while j < i:
#                 if i % j == 0:
#                     print(i,'不是质数')
#                     break
#                 j += 1
#             else:
#                 print(i,'是质数')         
#         i += 1