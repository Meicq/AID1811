# 计算社保
# 接受键盘输入的薪资并转化为数字
sal = float(input('请输入薪资:'))
# 定义变量,保存计算社保的薪资
shebao_sal = sal
if sal >19512:
    shebao_sal = 19512
elif 3902 <= sal <= 19152:
    shebao_sal = sal
elif 3902 * 0.175 <= sal < 3902:
    shebao_sal = 3902   
else:
    shebao_sal = 0      
print('应缴纳社保',shebao_sal*0.175)

