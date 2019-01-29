# 成绩判断程序
score = float(input('请输入成绩:'))
# 判断成绩
if score >= 90 and score <= 100:
    print('恭喜，成绩优秀')
elif score >= 80 and score < 90:
    print('恭喜，成绩良好')
elif score >= 60 and score < 80:
    print('恭喜，成绩合格')
elif score >= 0 and score < 60:
     print('抱歉，成绩不合格')
else:
    print('逗我玩呢？')
   