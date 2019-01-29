# 邮箱验证(yang@tedu.cn)
n = str(input('请输入邮箱:'))
if len(n) < 4:
	print('输入的邮箱有误！请重新输入...')
	n = str(input('请重新输入邮箱:'))
else:
	i = 0
	while i < len(n):
		if n[i] == '@':
			j = 0
			while j < len(n):
				if n[j] == '.':
					count = 0
					count += 1
				j += 1
				else:
					print('输入的邮箱有误！请重新输入...')
		else:
			

		i += 1

			if count == 2 or count == 3:
				print('邮箱输入正确！')
			else:
				print('输入的邮箱有误！请重新输入...')
