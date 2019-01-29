# 使用列表模拟'用户名,密码数据库',实现登录程序
import time
import getpass
name = input('请输入用户名:')
mima = getpass.getpass('请输入密码:')
names = ['mei','meicq','mcq','meichaoqian']
mimas = ['mei123','mcq123','meicq123']
isname = False
ismima = False
for x in names:
    if name == x:
        isname = True

for y in mimas:
    if mima == y:
        ismima = True

if isname and ismima:
    print('正在登录...')
    time.sleep(1)
    print('登录成功！')
else:
    print('用户名或密码错误！请重新输入')


