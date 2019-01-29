# 生成4位字符验证码
# 0(48)~9(57)   A(65)~Z(90)     a(97)~z(122)
# 思考,如何把所有的字符放在一起？
# chrs = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# 有多少字符？
chrs = ''
i = 48
while i <= 57:
    chrs += chr(i)
    i += 1
i = 65
while i <= 90:
    chrs += chr(i)
    i += 1
i = 97
while i <= 122:
    chrs += chr(i)
    i += 1
# print(chrs) # 打印输出字符串chrs

# 生成随机验证码
import random
yzm = ''
j = 1
while j <= 4:
    # 生成随机编号(索引)
    a = random.randint(0,len(chrs)-1)
    # 根据随机索引访问chrs中的字符
    ch = chrs[a]
    # 判断yzm中是否有ch
    n = 0
    isrepeat = False # 保存是否重复状态,默认不重复
    while n < len(yzm):
        if yzm[n] == ch: # 如果有一个字符相等
            isrepeat = True # 说明有重复
        n += 1
    if not isrepeat: # 如果没有重复
        yzm += ch # 把生成的随机字符增加到验证码中
        j += 1 # 验证码位数加1
print(yzm)





