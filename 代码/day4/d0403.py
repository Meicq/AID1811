# 输入一个字符串,把所有的a字符替换为b字符
s = input('请输入一个字符串:')
new_s = ''
i = 0
while i < len(s):
    # print(s[i])
    c = s[i]
    if c == 'a':
        new_s += 'b'
    else:
        new_s += c
    i += 1
print(new_s)

