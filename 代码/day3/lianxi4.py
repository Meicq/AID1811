# 打印九九乘法表
i = 1
while i <= 9: # 行
    j = 1
    while j <= i: # 列
        n = i * j
        print(i,'*',j,'=',n,end=' ') # 调整同行输出之间的分割,在end=''的单引号中加入空格
        # print(i,j,sep=' * ',end=' = '+str(i*j)+'  ')
        j += 1
    print()
    i += 1
    

