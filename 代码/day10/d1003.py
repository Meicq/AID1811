# 创建Cat类
class Cat():
    # 类的方法
    def __init__(self):
        # 类的属性
        self.name = 'miaomiao'
        self.age = 2
        self.weight = 12
    def cry(self):
        print(self.name+'猫正在叫')
    def sleep(self,adj):
        print('猫正在'+adj+'睡觉')
    def eat(self,food):
        print('猫正在吃'+food)
# 构建Cat对象
m1 = Cat()

m1.cry()
print(m1.name)

m1.name = 'Tom'
m1.cry()
print(m1.name)

m1.sleep('安静的')
m1.eat('鱼')
print(m1.name,m1.age,m1.weight)


# # 创建手机Phone类
# class Phone():
#     def __init__(self):
#         self.name = 'ViVo'
#         self.age = 2
#         self.price = 2200
#         self.property = '良好'
#     def pingpai(self,pp):
#         print('这款手机是'+pp+'的品牌')
#     def year(self,date):
#         print('这款手机是'+date+'上市的')
#     def photo(self,pixel):
#         print('这款手机像素是'+pixel)
#     def music(self,yinzhi):
#         print('这款手机音质'+yinzhi)
# # 构建对象
# p1 = Phone()
# p1.pingpai('华为')
# p1.year('2018.11.23')
# p1.photo('2200*1200')
# p1.music('非常优质')
# print('我的手机',p1.name,p1.age,p1.price,p1.property)

