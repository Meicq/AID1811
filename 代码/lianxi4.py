# 阿姆斯特朗数(水仙花数),n位数字的n次方之和等于自身
i = 100
while i <= 999999999999:
	n = len(str(i)) # 求位数
	j = 1
	num = 0
	b = i
	while j < n:
		a = b % 10
		b = b // 10
		num = num + a ** n
		j += 1
	num = num + b ** n
	if i == num:
		print(i)
	i += 1

