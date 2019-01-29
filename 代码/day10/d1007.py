# 定义小球的模型
class Sun():
    count = 1
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.color = 'red'
        self.direct = 'Right'
        self.speed = 3
        Sun.count += 1
        self.tag = 'SUN'+str(Sun.count)
    def draw(self,cvs):
        cvs.delete(self.tag)#根据标记删图画
        cvs.create_oval(self.x,self.y,\
            self.x+self.size,\
            self.y+self.size,\
            fill=self.color,\
            outline=self.color,\
            tag=self.tag
            )
    def step(self,cvs):
        if self.direct == 'Right':
            self.x += self.speed
        elif  self.direct == 'Left': 
            self.x -= self.speed
        elif self.direct == 'Down':
            self.y += self.speed
        elif self.direct == 'Up':
            self.y -= self.speed
        cvs.delete(self.tag)
        self.draw(cvs)
    def isbomb(self,food):
        if food.x-self.size <= self.x <= food.x+food.size:
            if food.y-self.size <= self.y <=food.y +food.size:
                return True

        
# 导入工具
import tkinter as tk
import random as rad
import time
# 创建窗体
window = tk.Tk()
# 设置标题
window.title('球球大作战')
# 修改窗体大小和位置
window.geometry('800x600+80+50')
# 创建画布
cvs = tk.Canvas(window,bg='#ABCDEF')
# 画布显示在整个窗体
cvs.pack(expand=tk.YES,fill=tk.BOTH)

s1 = Sun(300,300,50)
s1.draw(cvs)
ind = 0
foods = []
def food_enter():
    global ind
    ind += 1
    if ind % 1 == 0:
        x = rad.randint(0,800)
        y = rad.randint(0,600)
        size = rad.randint(10,20)
        food = Sun(x,y,size)
        colors = ['red','blue','green','yellow']
        i = rad.randint(0,len(colors)-1)
        food.color = colors[i]
        food.draw(cvs)
        foods.append(food)
def bomb():
    for food in foods:
        if s1.isbomb(food):
            cvs.delete(food.tag)
            foods.remove(food)
            s1.size += food.size

while True:
    s1.step(cvs)
    food_enter()
    # 吃食物(检测碰撞)
    bomb()
    #s1.out_of_bounds()
    #
    time.sleep(0.1)
    window.update()
#　显示窗体
window.mainloop()
