# 拆分字符串'libai,luna&xiaoqiao'
names = 'libai,luna&xiaoqiao'
a = names.split(sep=',') # 使用,拆分第一次
# print(a)
b = []
for name in a:
    # 第二次拆分,即可拆出人名
    # 每获取一个人名,放到列表b中
    b += name.split(sep='&')
print(b)



# 使用列表组合字符串'AaBbCc...Zz'
chrs = [] # 定义字母库,保存所有字母
for x in range(65,91):
    chrs.append(chr(x)) # 添加大写英文字母到列表中
    chrs.append(chr(x+32)) # 添加小写英文字母到列表中
# print(chrs)
s = ''.join(chrs) # 使用空字符串拼接列表为字符串
print(s)
