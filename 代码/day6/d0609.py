# 使用列表模拟'用户名,密码数据库',实现登录系统
names = ['libai','luna','yase']
pwds = ['123','456','789']
print('欢迎登录！！！')
n = input('请输入用户名：')
p = input('请输入密码：')
import os
os.system('clear')
# 实现登录的代码
if names.count(n) == 1:
    index = names.index(n)
    if pwds[index] == p:
        print('登录成功！')
    else:
        print('密码输入有误！')
else:
    print('用户名不存在！')

