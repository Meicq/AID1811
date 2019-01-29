# 有10000个数据样本,统计其中每个数据出现的次数
# 1.获取数据
# dates = ['a','x','1','中','1','a','1']
# 2.数据样本去重
# date = ['a','x','1','中']
# 3.判断date中每个元素在dates中出现的次数
# cs = [2,1,3,1]
# 4.排序:
# cs = [3,2,1,1]
# 5.找到出现次数最多的字符

# 1.准备数据
import random as rad
chrs = []
for x in range(10000):
    n = rad.randint(19000,19100)
    chrs.append(chr(n))
# print(chrs)
# 2.对数据去重
chs = []
for ch in chrs:
    if ch not in chs:
        chs.append(ch)
# print(chs)
# 3.判断每个数据出现的次数
counts = []
for x in chs:
    counts.append(chrs.count(x))
print(counts)
# 4.从大到小对counts中的数据排序
cons = counts.copy()
cons.sort(reverse=True)
print(cons)
# 5.查询出现次数最多的前几个字符 
for x in range(10):
    index = counts.index(cons[x])
    print(chs[index],'出现了',cons[x],'次')
    # bug:当有两个字符出现次数相同的时候,再回去索引字符的时候只会找到第一个出现这个次数的字符
    # 解决方法
    chs.remove(chs[index])
    counts.remove(cons[x])


# 生成10000个0~9之间的数字,判断每个数字出现的次数
# 方法1
# import random as rad
# nums = []
# for x in range(10000):
#     nums.append(rad.randint(0,9))
# for y in range(0,10):
#     print(y,'出现了',nums.count(y))








# # 生成10000个0~9之间的数字,判断每个数字出现的次数
import random as rad
def cishu(n):
    L = []
    for x in range(10000):
        num = rad.randint(0,9)
        L.append(num)
    return L.count(n)

print(cishu(0))
print(cishu(1))
print(cishu(2))
print(cishu(3))
print(cishu(4))
print(cishu(5))
print(cishu(6))
print(cishu(7))
print(cishu(8))
print(cishu(9))
