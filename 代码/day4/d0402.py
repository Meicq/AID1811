# 2.从键盘输入一个字符串,遍历
# 3.在2的基础上,统计其中a和b字符出现的次数
s = str(input('请输入一串字符串:'))
i = 0
n_a = 0
n_b = 0
while i < len(s):
    print(s[i]) # 打印输出字符串的遍历
    if s[i] == 'b':
        n_b += 1
    if s[i] == 'a':
        n_a += 1

    i += 1
print('字符a出现的次数为:',n_a)
print('字符b出现的次数为:',n_b)




