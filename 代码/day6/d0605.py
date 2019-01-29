# 保存班级学生成绩到列表中,计算max,min,avg
n = int(input('请输入学生人数：'))
i = 1
L = []
while i <= n:
    score = int(input('请输入学生成绩：'))
    L.append(score)
    i += 1
print('学生的成绩：',L)
j = 0
sum = 0
max = min = L[0]
while j < n:
    if L[j] > max:
        max = L[j]
    if L[j] < min:
        min = L[j]
    sum = sum + L[j]
    j += 1
print('学生的成绩最高分：',max,'最低分：',min,'平均分：',avg)


