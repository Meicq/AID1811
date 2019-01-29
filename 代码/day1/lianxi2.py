# 模拟滴滴打车的计费,计时系统
# 输入距离
juli = float(input('请输入距离:'))
# 计算时长,距离 / 速度
shijian = juli / 50
xiaoshi = shijian // 1
fenzhong = (shijian - xiaoshi) * 60 // 1
# 下行代码是设置精度，取小数后两位
# fenzhong = round(fenzhong,2)
# 计算费用,起步价 + 每公里费用
feiyong = (13 + 2.3 * juli) // 1
print('预估时长:',shijian,'小时')
print('预估时长:',xiaoshi,'小时',fenzhong,'分钟')
print('费用:',feiyong,'元')