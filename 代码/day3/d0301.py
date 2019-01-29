# 输入5个学生成绩,计算最高分,最低分和平均分
# 1.写一个循环5次的循环
i = 1 # 循环条件的初始化,人数
sum = 0 # 定义变量sum,用来保存总成绩
max = min = 0
while i <= 5:
    sco = float(input('请输入第'+str(i)+'个学生成绩'))
    if i == 1:
        max = min = sco
    else:
        if sco > max:
            max = sco
        if sco < min:
            min = sco
    print('最高分:',max,'最低分:',min)
    sum = sum + sco
    print('平均分:',sum/i)
    i += 1 