# 邮箱验证
yx = input('请输入邮箱:')
isyx = True
yhm = yx[:yx.find('@')] # index = yx,find('@')\yhm = yx[:index]
if not len(yhm) >= 4:
    isyx = False
if not yx.count('@') == 1:
    isyx = False
if not yx.count('.') == 1 or yx.count('.') == 2:
    isyx = False
if isyx:
    print('邮箱验证正确！')
else:
    print('邮箱输入有误！')

