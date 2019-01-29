# 排序－－－－冒泡排序法
L = [1,35,63,3,36,26,7]
print(L[４])
for x in L:
    for x in range(len(L)):
        if L[x] > L[x+1]:
            m = L[x]
            L[x] = L[x+1]
            L[x+1] = m
print(L)

