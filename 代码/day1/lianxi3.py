# 计算下载一部小说需要多少流量
# 输入小说的数字
num = int(input('请输入小说的数字:'))
# 计算需要多少M流量
count = float(num * 3 / 1024 / 1024)
count = round(count,8)
print('总共需要',count,'M流量')