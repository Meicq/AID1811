# 随机生成100个100~999之间的数字,统计其中512出现的次数
import random as rad # 导入random并给别名rad(重命名)
i = 1
j = 0
while i <= 10000:
    n = rad.randint(100,200)
    if n == 149:
        j += 1
    i += 1
print('512出现的次数有:',j,'次')