# 质数问题
n = 1
while n <= 100:
    i = 2
    while i <= n-1:
        if n % i == 0:
            print(n,'不是质数')
            break
        i += 1
    else:
        print(n,'是质数')
    n += 1