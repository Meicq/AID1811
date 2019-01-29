# 超市收银系统
count = input('请输入商品数量:')
# 商品的数量有可能是小数，所以使用float
count = float(count)
price = input('请输入商品价格:')
price = float(price)
# 计算消费金额
money = count * price
print('一共消费:',money,'元')
# 输入消费金额
money1 = input('请输入收取金额:')
money1 = float(money1)
# 计算找零
case = money1 - money
print('找零:',case,'元')


# 社保 = 薪资 * 0.175
xinzi = input('请输入薪资:')
xinzi = float(xinzi)
shebao = xinzi * 0.175
print('社保:',shebao)

# 输入半径,计算圆的周长和面积
R = float(input('输入圆的半径:'))
# 上面这一行代码等同于下面两行代码
# R = input('输入圆的半径:')
# R = float(R)
l = 2 * 3.14 * R
S = 3.14 * R ** 2
print('圆的周长:',l)
print('圆的面积:',S)

