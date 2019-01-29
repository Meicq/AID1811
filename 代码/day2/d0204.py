# 登录问题
name = input('请输入用户名:')
# pwd = input('请输入密码:')
import getpass # 导入getpass工具
# 实现密码的暗文输入
# getpass.getpass()其中'.'号前面的getpass表示使用getpass工具,'.'号后面的getpass()表示工具里面的一种方法
pwd = getpass.getpass('请输入密码:')
import time # 导入时间time工具
print('正在登录...')
time.sleep(2) # 系统休眠2s
# 登录
if name == 'admin' and pwd == '123':
    print('登录成功！')
else:
    print('登录失败！')
