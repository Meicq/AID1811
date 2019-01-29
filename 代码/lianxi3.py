# 斐波那契数列(兔子数量)
year = int(input('请输入年数：'))
i = 1
count = 1
while i <= year:
	if i == 1: # 第一代兔子的数量
		num1 = count
		# print('第',i,'年的兔子的数量是：',num1)
		print(num1,end=',')
	elif i == 2: # 第二代兔子的数量
		num2 = count
		# print('第',i,'年的兔子的数量是：',num2)
		print(num2,end=',')
	else: # 第三代到第n代兔子的数量
		num3 = num2 + num1
		num1 = num2
		num2 = num3
		# print('第',i,'年的兔子的数量是：',num3)
		print(num3,end=',')
	i += 1


