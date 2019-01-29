# 1.登录系统
import getpass
import time
import os

print('1:注册')
print('2:登陆')
shuru = input('请输入1或者2:')

if shuru == '1':
    # 注册程序
    # 用户名注册
    print('欢迎注册：')
    isname = True  # 用户名默认正确
    name = input('请输入名称:')
    # 用户名长度５～１０位
    length = len(name)
    if not 5 <= length <= 10:
        isname = False
    #　列出所有合法字符
    chrs = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    # 判断name中每一个字符是否合法
    i = 0
    while i < len(name):
        if chrs.count(name[i]) == 0:
            isname = False
        i += 1
    if isname:
        print('用户名正确')
    else:
        print('用户名不合法')
    # 密码注册
    pwd = input('请输入密码:')
    repwd = input('请再次输入密码:')
    ispwd = True
    if pwd != repwd:ispwd = False
    if len(pwd) != 6:ispwd = False
    i = 0
    while i < len(pwd):
        code = ord(pwd[i])
        if not 48<=code<=57:
            ispwd = False
        i += 1
    if ispwd:
        print('密码合法')
    else:
        print('密码输入不合法')



        
if shuru == '2':
    name = input('请输入用户名:')
    mima = getpass.getpass('请输入密码:')
    while name != 'meicq' or mima != '123456':
        print('用户名或密码错误！请重新输入')
        name = input('请输入用户名:')
        mima = getpass.getpass('请输入密码:')
    else:
        print('正在登录...')
        time.sleep(1)
        print('登录成功！')
# # 2.选择城市
# city = input('请选择城市:')
# bj_sal = 10712
# sh_sal = 10128
# sz_sal = 9738
# hz_sal = 9547
# gz_sal = 7862
# wh_sal = 7104
# if city == '北京':
#     pj_sal = bj_sal
# elif city == '上海':
#     pj_sal = sh_sal
# elif city == '深圳':
#     pj_sal = sz_sal
# elif city == '杭州':
#     pj_sal = hz_sal
# elif city == '广州':
#     pj_sal = gz_sal
# elif city == '武汉':
#     pj_sal = wh_sal
# print(city,'社保上限为:',pj_sal*3)
# print(city,'社保下限为:',pj_sal*0.6)
# # 3.输入薪资,计算社保
# sal = float(input('请输入薪资:'))
# shebao_sal = sal
# if sal > pj_sal * 0.6:
#     shebao_sal = pj_sal * 0.6
# elif pj_sal * 3 <= sal <= pj_sal * 0.6:
#     shebao_sal = sal
# elif pj_sal * 3 * 0.175 <= sal < pj_sal * 3:
#     shebao_sal = pj_sal * 3   
# else:
#     shebao_sal = 0      
# print('应缴纳社保:',shebao_sal*0.175)
# # 4.计算纳税
# # sale = float(input('请输入薪资:'))
# X = sal - 5000
# if X <= 0:
#     nashui = 0
# elif 0 < X <= 1500:
#     nashui = X * 0.03 - 0
# elif 1500 < X <= 4500:
#     nashui = X * 0.10 - 105
# elif 4500 < X <= 9000:
#     nashui = X * 0.20 - 555
# elif 9000 < X <= 35000:
#     nashui = X * 0.25 - 1005
# elif 35000 < X <= 55000:
#     nashui = X * 0.30 - 2755
# elif 55000 < X <= 80000:
#     nashui = X * 0.35 - 5505
# elif X > 80000:
#     nashui = X * 0.45 - 13505
# print('应纳税金额:',nashui)


