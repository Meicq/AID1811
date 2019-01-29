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

def listener(event):
    if event.keysym =='Up':
        head[6] = 'Up'
    elif event.keysym == 'Down':
        head[6] = 'Down'
    elif event.keysym == 'Left':
        head[6] = 'Left'
    elif event.keysym == 'Right':
        head[6] = 'Right'
# 安装监听器，调用listener函数
window.bind('<Key>',listener)

lenth = 2
size = 10
head = [100,100,110,110,'red','red','Left','head']
tail = [100+(lenth-1)*10,100,110+(lenth-1)*10,110,'blue','red','Left','tail']
# body = [0,0,0,0,'blue','red','0']

cvs.create_rectangle(head[0],head[1],head[0]+size,head[1]+size,fill=head[4],outline=head[5],tag=head[7])
cvs.create_rectangle(tail[0],tail[1],tail[2],tail[3],fill=tail[4],outline=tail[5],tag=tail[7])

foods = []
count = 1
def food_enter():
    global count
    x = random.randint(0,790)
    y = random.randint(0,590)
    size = 10
    food = [x,y,x+size,y+size,'yellow','yellow',str(count)]
    cvs.create_rectangle(food[0],food[1],food[0]+size,food[1]+size,fill=food[4],outline=food[5],tag=food[6])
    foods.append(food)
    count += 1

def step_action():
    step = 10
    # 根据方向移动小球
    if head[6] == 'Right':
        cvs.move(head[7],step,0)
        head[0] += step
        if tail[6] != head[6]:
            cvs.move(tail[7],step,0)
            tail[0] += step
        tail[6] = head[6]
        cvs.move(tail[7],step,0)
        tail[0] += step
    elif head[6] == 'Left':
        cvs.move(head[7],-step,0)
        head[0] -= step
        if tail[6] != head[6]:
            cvs.move(tail[7],-step,0)
            tail[0] -= step
        tail[6] = head[6]
        cvs.move(tail[7],-step,0)
        tail[0] -= step
    elif head[6] == 'Up':
        cvs.move(head[7],0,-step)
        head[1] -= step
        if tail[6] != head[6]:
            cvs.move(tail[7],0,-step)
            tail[1] -= step
        tail[6] = head[6]
        cvs.move(tail[7],0,-step)
        tail[1] -= step
    elif head[6] == 'Down':
        cvs.move(head[7],0,step)
        head[1] += step
        if tail[6] != head[6]:
            cvs.move(tail[7],0,step)
            tail[1] += step
        tail[6] = head[6]
        cvs.move(tail[7],0,step)
        tail[1] += step


while True:
    food_enter()
    step_action()
    time.sleep(0.1)
    window.update()


         



# 显示窗体
window.mainloop()
