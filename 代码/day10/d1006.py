# 定义小球的模型
class Sun():
    count = 1
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.color = 'red'
        self.direct = 'right'
        self.speed = 5
        Sun.count += 1
        self.tag = 'SUN'+str(Sun.count)

    def draw(self,cvs):
        cvs.delete(self.tag)# 根据标记删除图画
        cvs.create_oval(self.x,self.y,self.x+self.size,self.y+self.size,fill=self.color,\
        outline=self.color,tag=self.tag)

    def step_action(self):
        if self.direct == 'Right':
            cvs.move(self.tag,self.speed,0)
            self.x += self.speed
        elif self.direct == 'Left':
            cvs.move(self.tag,-self.speed,0)
            self.x -= self.speed
        elif self.direct == 'Up':
            cvs.move(self.tag,0,-self.speed)
            self.y -= self.speed
        elif self.direct == 'Down':
            cvs.move(self.tag,0,self.speed)
            self.y += self.speed

    def out_of_bounds(self):
        if self.x >= 800 - self.size:
            self.direct = 'Left'
        elif self.x <= 0:
            self.direct = 'Right'
        elif self.y >= 600 - self.size:
            self.direct = 'Up'
        elif self.y <= 0:
            self.direct = 'Down'

    def isbomb(self,food):
        if food.x - self.size <= self.x <= food.x + food.size:
            if food.y - self.size <= self.y <= food.y + food.size:
                return True
    


# 导入工具
import tkinter as tk
import time,random
# 创建窗体
window = tk.Tk()
# 设置窗体标题
window.title('球球大作战')
# 设置窗体大小
window.geometry('800x600+112+76')
# 创建画布
cvs = tk.Canvas(window,bg='#ABCDEF')
# 画布显示
cvs.pack(expand=tk.YES,fill=tk.BOTH)

#　创建小球对象和画出小球对象
s1 = Sun(300,300,50)
s1.draw(cvs)

# 创建食物小球对象和画出食物小球对象
foods = []
n = 0
def foods_enter():
    global n
    n += 1
    if n % 20 == 0:
        x = random.randint(0,800)
        y = random.randint(0,600)
        size = random.randint(10,20)
        food = Sun(x,y,size)
        colors = ['red','blue','yellow','green','grey','black']
        food.color = colors[random.randint(0,len(colors)-1)]
        food.draw(cvs)
        foods.append(food)

def bomb():
    for food in foods:
        if s1.isbomb(food):
            if food.color == 'black':
                s1.size -= 20
            else:
                s1.size += 3
            cvs.delete(food.tag)
            foods.remove(food)
            s1.draw(cvs)


def listener(event):
    if event.keysym =='Up':
        s1.direct = 'Up'
    elif event.keysym == 'Down':
        s1.direct = 'Down'
    elif event.keysym == 'Left':
        s1.direct = 'Left'
    elif event.keysym == 'Right':
        s1.direct = 'Right'
# 安装监听器，调用listener函数
window.bind('<Key>',listener)

while True:
    s1.step_action()
    foods_enter()
    bomb()
    s1.out_of_bounds()
    time.sleep(0.01)
    window.update()


# 显示窗体
window.mainloop()


# s1 = Sun(1,1,10)
# s2 = Sun(2,2,10)
# print(s1.tag,s2.tag)
