# 计算城市社保上下限
# 从键盘输入城市
name = input('请输入城市名:')
bj_sal = 15000
sh_sal = 12000
sz_sal = 10000
if name == 'beijing':
    sal = bj_sal
elif name == 'shanghai':
    sal = sh_sal
elif name == 'shenzhen':
    sal = sz_sal
print(name,'社保上限为:',sal*3)
print(name,'社保下限为:',sal*0.6)


