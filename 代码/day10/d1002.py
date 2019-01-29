# 创建类
class Dog():
    def __init__(self):
        self.name = 'wangcai'
        self.age = 3
        print('构造方法被调用了！')
    def sleep(self,adj):
        print('狗正在'+adj+'睡觉．．．')
    def eat(self,adj1):
        print('狗正在'+adj1+'吃．．．')
# 构建对象
d1 = Dog()
d1.sleep('安静的')
d1.eat('尽情的')
print(d1.name,d1.age)
d1.name = 'ahuang'
print(d1.name,d1.age)
# d2 = Dog()
# d2.sleep('翻来覆去')
# d2.eat('狼吞虎咽的')

