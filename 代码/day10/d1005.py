# 定义小球的模型
class Sun():
    count = 1
    def __init__(self,x,y,size,direct):
        self.x = x
        self.y = y
        self.size = size
        self.color = 'red'
        self.direct = direct
        self.speed = 3
        Sun.count += 1
        self.tag = 'SUN'+str(Sun.count)

    def draw(self,cvs):
        cvs.delete(self.tag)# 根据标记删除图画
        cvs.create_oval(self.x,self.y,self.x+self.size,self.y+self.size,fill=self.color,\
        outline=self.color,tag=self.tag)

    def step_action(self,step):
        if self.direct == 'Right':
            cvs.move(self.tag,step,0)
            self.x += step
        elif self.direct == 'Left':
            cvs.move(self.tag,-step,0)
            self.x -= step
        elif self.direct == 'Up':
            cvs.move(self.tag,0,-step)
            self.y -= step
        elif self.direct == 'Down':
            cvs.move(self.tag,0,step)
            self.y += step

    def out_of_bounds(self):
        if self.x >= 800 - self.size:
            self.direct = 'Left'
        elif self.x <= 0:
            self.direct = 'Right'
        elif self.y >= 600 - self.size:
            self.direct = 'Up'
        elif self.y <= 0:
            self.direct = 'Down'


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

s1 = Sun(300,300,50,'Right')
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
    s1.step_action(20)
    s1.out_of_bounds()
    time.sleep(0.01)
    window.update()


# 显示窗体
window.mainloop()


# s1 = Sun(1,1,10)
# s2 = Sun(2,2,10)
# print(s1.tag,s2.tag)
