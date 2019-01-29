# 保存班级学生成绩到列表中,计算max,min,avg
scores = []
while True:
    score = input('请输入学生成绩：')
    if score == 'q':
        break
    score = int(score)
    scores.append(score)


print('最高分：',max(scores)) # 直接使用求最大数的内建函数max
print('最低分：',min(scores)) # 直接使用求最小数的内建函数min
print('平均分：',sum(scores)/len(scores)) # 使用求和的内建函数sum


