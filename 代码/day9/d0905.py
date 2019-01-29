# 扑克牌－斗地主发牌程序
# 准备牌库
pukes = []
huase = ['黑桃','红桃','梅花','方块']
for x in range(1,14):
    if x == 1:
        for y in huase:
            pukes.append(y+'A')
    elif x == 11:
        for y in huase:
            pukes.append(y+'J')
    elif x == 12:
        for y in huase:
            pukes.append(y+'Q')
    elif x == 13:
        for y in huase:
            pukes.append(y+'K')
    else:
        for y in huase:
            pukes.append(y+str(x))
pukes.extend(['大王','小王'])
# print(pukes)
# 发牌----------------------------------------
import random as rad
def fapai():
    shoupai = []
    for x in range(17):
        # 生成随机索引
        index = rad.randint(0,len(pukes)-1)
        # 拿出对应牌
        pai = pukes[index]
        shoupai.append(pai) # 添加到手牌中
        pukes.remove(pai) # 牌库中移除此牌
    return shoupai

print('玩家１手牌：',fapai())
print('玩家２手牌：',fapai())
print('玩家３手牌：',fapai())
print('底牌：',pukes)



# # 优化后代码
# # 准备牌库
# pukes = []
# huase = ['黑桃','红桃','梅花','方块']
# def fun(ty):
#     for y in huase:
#         pukes.append(y+ty)
# for x in range(1,14):
#     if x == 1:
#         fun('A')
#     elif x == 11:
#         fun('J')
#     elif x == 12:
#         fun('Q')
#     elif x == 13:
#         fun('K')
#     else:
#         fun(str(x))
# pukes.extend(['大王','小王'])
# print(pukes)
# # 发牌----------------------------------------
# import random as rad
# def fapai():
#     shoupai = []
#     for x in range(17):
#         # 生成随机索引
#         index = rad.randint(0,len(pukes)-1)
#         # 拿出对应牌
#         pai = pukes[index]
#         shoupai.append(pai) # 添加到手牌中
#         pukes.remove(pai) # 牌库中移除此牌
#     return shoupai

# print('玩家１手牌：',fapai())
# print('玩家２手牌：',fapai())
# print('玩家３手牌：',fapai())
# print('底牌：',pukes)
