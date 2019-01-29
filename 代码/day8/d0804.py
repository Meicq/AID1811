# 实现注册系统
# 内置用户名和密码
names = ['libai','luna','ake']
pwds = ['123','456','789']

# 自定义注册函数
def zhuce(name,pwd,repwd):
    if names.count(name) == 1:
        print('用户名已经存在！')
        return

    if pwd != repwd:
        print('密码输入不一致！')
        return
    
    names.append(name)
    pwds.append(pwd)
    return True

# 调用函数
name = input('请输入用户名：')
pwd = input('请输入密码：')
repwd = input('请重新输入密码：')
if zhuce(name,pwd,repwd):
    print('用户注册成功！')
else:
    print('用户注册失败！')
    
    

