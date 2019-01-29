# # 录入班级学生成绩,计算最高分,最低分,平均分
# # 获取班级学生人数
# n = int(input('请输入班级学生人数:'))
# i = 1
# sum = max = min = 0
# while i <= n:
#     score = float(input('请输入第'+str(i)+'位学生成绩:'))
#     if i == 1:
#         max = min = score
#     elif score > max:
#         max = score
#     elif score < min:
#         min = score
#     sum = sum + score
#     avg = sum / n
#     i += 1
# print('学生成绩最高分:',max,'最低分:',min,'平均分:',avg)


# 录入班级学生成绩,计算最高分,最低分,平均分
i = 1
sum = max = min = count = 0
while True:
    score = float(input('请输入第'+str(i)+'位学生成绩:'))
    if score == 'q':
        break
    count += 1
    if i == 1:
        max = min = score
    elif score > max:
        max = score
    elif score < min:
        min = score
    sum = sum + score
    avg = sum / i
    i += 1
    print('一共有',count,'名学生')
    print('学生成绩最高分:',max,'最低分:',min,'平均分:',avg,'总分:',sum)