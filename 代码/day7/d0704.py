# 机选双色球
# 红球和蓝球的球库
reds = []
blues = []
for x in range(1,34):
    if x < 10:
        reds.append('0'+str(x))
        blues.append('0'+str(x))
    elif x <= 16:
        reds.append(str(x))
        blues.append(str(x))
    else:
        reds.append(str(x))   
# print(reds)
# print(blues)
# 机选一注的逻辑实现
import random
rc = []
i = 1
while i <= 6:
    # 生成随机数字
    index = random.randint(0,32)
    # 根据随机数字拿到随机号码
    red = reds[index]
    if rc.count(red) == 0:
        rc.append(red) # 把红球添加到选中的库中
        i += 1
print('红球：',rc)
bc = blues[random.randint(0,15)]
print('蓝球：',bc)


