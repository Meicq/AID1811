# 回声聊天机器人-实现敏感词屏蔽
while True:
    msg = input('请输入你要说的话：')
    if msg == 'q':
        break
    msg = msg.replace('不会玩','***')
    msg = msg.replace('cao','***')
    msg = msg.replace('我去','**')
    print('robot:',msg)