# 阿姆斯特朗数(水仙花数),n位数字的n次方之和等于自身
n = 100
while n <= 10**12 - 1:
    s = str(n) # 数字转化为字符串
    # 取出字符串中每一个字符
    i,sum = 0,0
    while i < len(s):
        num = int(s[i])
        sum += num ** len(s)
        i += 1
    if n == sum:
        print(n)
    n += 1

