# 实现注册系统
# 准备数据库
names = ['libai','luna']
pwds = ['123','456']
isreg = True
# 注册
while True:
    name = input('请输入用户名：')
    if names.count(name) == 1:
        isreg = False
        print('用户名已经存在！')
    else:
        isreg = True
        print('用户名有效！')
        break

# 密码验证
pwd = input('请输入密码：')
repwd = input('请再次输入密码：')
if len(pwd) < 6 or pwd != repwd:
    print('密码输入有误！')
    isreg = False
else:
    isreg = True

# 随机生成6位验证码验证
import random
chrs = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
i = 1
yzm = ''
while i <= 6:
    index = random.randint(0,len(chrs)-1)
    ch = chrs[index]
    yzm = yzm + ch
    i += 1
print(yzm)
yzm_sr = input('请输入验证码：')
if yzm == yzm_sr:
    print('验证码输入正确！')
    isreg = True
else:
    print('验证码输入错误，注册失败！')
    isreg = False

if isreg:
    names.append(name)
    pwds.append(pwd)
    print('注册成功！')
    print(names)
    print(pwds)



