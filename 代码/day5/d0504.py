# 有数据'a.jpg,b.mp4,d.py,d.java,d.c,g.py'
# 要求1：筛选出所有的python文件
# 要求2：打印出以文件名是d的所有文件
s = 'a.jpg,b.mp4,d.py,d.java,d.c,g.py'
count = s.count(',') # 查询','出现的次数
i = 1 # 用来协助循环
while i <= count+1:
    ind = s.find(',') # 查询','出现的第一个索引
    if ind == -1: # 如果查询不到','
        name = s # 剩余的字符就是文件名
    else: # 能找到','，通过切片获取文件名
        name = s[:ind]
    if name.endswith('.py'):
        print(name)
    s = s[ind+1:]
    i += 1


