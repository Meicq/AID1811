# 斐波那契数列
start,end = 1,1
n = 1
while n <= 20:
    if n == 1 or n == 2:
        end = 1
    else:
        start,end = end,start + end
    print('第',n,'代兔子数量是',end,'只')
    n += 1
