# 打印输出100以内的所有的质数
# 打印输出n以内的所有的质数
n = int(input('请输入一个数：'))
i = 2
while i <= n:
	if i == 2:
		print('100以内的质数有：',i,end=',')
	elif i > 2:
		j = 2
		count = 0
		while j < i:
			if i % j == 0:
				count += 1
			j += 1
		if count == 0:
			print(i,end=',')
	i += 1


# # 优化修改
# n = int(input('请输入一个数：'))
# i = 2
# while i <= n:
# 	if i >= 2:
# 		j = 2
# 		count = 0
# 		while j < i:
# 			if i % j == 0:
# 				count += 1
# 			j += 1
# 		if count == 0:
# 			print(i,end=',')
# 	i += 1




