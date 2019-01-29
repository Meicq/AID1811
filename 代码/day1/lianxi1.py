# 财务系统-->缴纳社保
# 输入薪资
xinzi = float(input('请输入薪资:'))
# 计算公司缴纳的社保,薪资 * 0.42
gs_shebao = xinzi * 0.42
# 计算个人缴纳的社保,薪资 * 0.175
gr_shebao = xinzi * 0.175
# 计算实际到手薪资,薪资 - 个人社保
sj_xinzi = xinzi - gr_shebao
print('公司缴纳社保:',gs_shebao)
print('个人缴纳社保:',gr_shebao)
print('实际到手薪资:',sj_xinzi)