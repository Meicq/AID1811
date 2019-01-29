# 猜数字小游戏
print('-----------------')
print('欢迎来到猜数字小游戏')
print('-----------------')
input('请输入任意字符继续...')
print('正在生成随机数...')
import time
time.sleep(2)
# 1.随机生成一个要猜测的数字
import random
n = random.randint(1,100)
print('已经生成随机数,开始猜测吧！')
score = 100
while score > 0:
    guess = int(input('请输入您猜测的数字:'))
    if guess > n:
        print('抱歉,您猜大了！')
    elif guess < n:
        print('抱歉,您猜小了！')
    else:
        print('恭喜您,您猜对了！','最终得分:',score,'分')
        break
    score -= 5
else:
    print('您猜测的数字是:',n,'最终得分:0分')

