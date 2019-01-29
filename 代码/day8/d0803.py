# 登录程序
# 内置用户名和密码
names = ['libai','luna','ake']
pwds = ['123','456','789']

# 使用自定义函数登录
def login(name,pwd):
    name = name.strip() # 去除字符串两端的空格
    if names.count(name) == 0:
        print('用户名不存在！')
        return
    # 查询names中name的索引
    index = names.index(name)
    if pwd != pwds[index]:
        print('密码错误！')
        return
    return True

# 实现登录
name,pwd = input('用户名：'),input('密码：')
if login(name,pwd):
    print('login success')
else:
    print('login fail')