# 计算水仙花数(水仙花数是指三位数的每位数字的三次方之和等于自身)
# 打印输出100~999
i = 100
while i <= 999:
    # 获取百位的值
    i_baiwei = i // 100 # i_baiwei = i // 10 // 10
    # 获取十位的值
    i_shiwei = i // 10 % 10
    # 获取各位的值
    i_gewei = i % 10 
    if i == i_baiwei ** 3 + i_shiwei ** 3 + i_gewei ** 3:
        print(i,'是水仙花数')
    # else:
    #     print(i,'不是水仙花数')
    i += 1




