# 计算利滚利滚利(复利计算)
# 数据的问题(定存金额,年利率,存款年限)
amount = float(input('输入定存金额:'))
n = int(input('输入存款年限:'))
rate = float(input('输入年利率:'))
i = 1
sum = 0
while i <= n: # 存款年限
    sum = sum + amount # 年初存款
    sum = sum + sum * rate
    # 上两行代码可以合并为一行:sum = (sum + amount) * (1 + rate)
    sum = round(sum,2)
    print('第',i,'年卡内金额:',sum)
    i += 1
print(n,'年后卡内余额:',sum)
