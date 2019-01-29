# names = 'libai,luna,wangzhaojun,yase'
# 从names字符串中拆除每个人的姓名并打印输出。
# 输入姓名字符串，姓名之间用'，'隔开
names = 'libai,luna,wangzhaojun,yase'
count = names.count(',')
i = 1
while i <= count:
    name = names[:names.find(',')]
    names = names[names.find(',')+1:]
    print('第',i,'名学生的姓名是:',name)
    i += 1
print('第',i,'名学生的姓名是:',names)



# # 方法一:
# s = 'libai,luna,wangzhaojun,yase,zhaoyun'
# name = ''
# i = 0
# while i < len(s):
#     if s[i] != ',':
#         name += s[i]
#     else:
#         print(name)
#         name = ''
#     i += 1
# print(name)





# # 方法二:
# s = 'libai,luna,wangzhaojun,yase,zhaoyun'
# start = 0
# end = 0
# i = 0
# isover = False
# while not isover:
#     i += 1
#     if i == 1:
#         end = s.find(',')
#         name = s[0:end]
#     else:
#         start = end + 1
#         end = s.find(',',end+1)
#         if end == -1:
#             isover = True
#             name = s[start:]
#         else:
#             name = s[start:end]
#     print(name)
#     # 上面循环语句部分简化版
#     # i += 1
#     # end = s.find(',',end+1)
#     # name = s[start:end]
#     # start = end + 1
#     # print(name)




