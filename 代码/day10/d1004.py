import random as rad
import time
# 创建一个英雄类
class Hero():
    def __init__(self,name,blood):
        self.name = name
        self.blood = blood
    def attack(self,emy):
        hurt = rad.randint(9,21)
        emy.blood -= hurt
        return hurt

# 构建两个英雄对象
h1 = Hero('yase',100)
h2 = Hero('xiangyu',100)

# 实现对战
i = 0
while True:
    i += 1
    time.sleep(1)
    hurt = h1.attack(h2)
    print(h1.name,'攻击',h2.name,'造成了',hurt,'点伤害')
    if h2.blood <= 0:
        h2.blood = 0
        print(h2.name,'剩余血量',h2.blood)
        break
    print(h2.name,'剩余血量',h2.blood)

    hurt = h2.attack(h1)
    print(h2.name,'攻击',h1.name,'造成了',hurt,'点伤害')
    if h1.blood <= 0:
        h1.blood = 0
        print(h1.name,'剩余血量',h1.blood)
        break
    print(h1.name,'剩余血量',h1.blood)
    print('第',i,'回合结束！')
    print('=========================================')



