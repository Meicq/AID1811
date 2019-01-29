# 财务系统-纳税计算
xinzi = float(input('请输入薪资:'))
X = xinzi - 5000
if X <= 0:
    nashui = 0
elif 0 < X <= 1500:
    nashui = X * 0.03 - 0
elif 1500 < X <= 4500:
    nashui = X * 0.10 - 105
elif 4500 < X <= 9000:
    nashui = X * 0.20 - 555
elif 9000 < X <= 35000:
    nashui = X * 0.25 - 1005
elif 35000 < X <= 55000:
    nashui = X * 0.30 - 2755
elif 55000 < X <= 80000:
    nashui = X * 0.35 - 5505
elif X > 80000:
    nashui = X * 0.45 - 13505
print('应纳税金额:',nashui)
    
