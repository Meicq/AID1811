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

sun = [300,300,50,'Right','SUN']
colors = ['red','yellow','blue','black','green']
# 画小球模型
cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[0],outline=colors[0],tag=sun[4])

# time.time()获取按键的时间

def listener(event):
    if event.keysym =='Up':
        sun[3] = 'Up'
    elif event.keysym == 'Down':
        sun[3] = 'Down'
    elif event.keysym == 'Left':
        sun[3] = 'Left'
    elif event.keysym == 'Right':
        sun[3] = 'Right'
# 安装监听器，调用listener函数
window.bind('<Key>',listener)

def step_action():
    step = 20
    # 根据方向移动小球
    if sun[3] == 'Right':
        cvs.move(sun[4],step,0)
        sun[0] += step
    elif sun[3] == 'Left':
        cvs.move(sun[4],-step,0)
        sun[0] -= step
    elif sun[3] == 'Up':
        cvs.move(sun[4],0,-step)
        sun[1] -= step
    elif sun[3] == 'Down':
        cvs.move(sun[4],0,step)
        sun[1] += step
    # 控制小球移动变色
    if sun[3] == 'Right' or sun[3] == 'Left':
        # 控制小球在x方向移动变色
        if sun[0] //step % 5 == 0:
            cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[0],outline=colors[0],tag=sun[4])
        elif sun[0] //step % 5 == 1:
            cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[1],outline=colors[1],tag=sun[4])
        elif sun[0] //step % 5 == 2:
            cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[2],outline=colors[2],tag=sun[4])
        elif sun[0] //step % 5 == 3:
            cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[3],outline=colors[3],tag=sun[4])
        elif sun[0] //step % 5 == 4:
            cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[4],outline=colors[4],tag=sun[4])
    elif sun[3] == 'Up' or sun[3] == 'Down':
        # 控制小球在y方向移动变色
        if sun[1] //step % 5 == 0:
            cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[0],outline=colors[0],tag=sun[4])
        elif sun[1] //step % 5 == 1:
            cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[1],outline=colors[1],tag=sun[4])
        elif sun[1] //step % 5 == 2:
            cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[2],outline=colors[2],tag=sun[4])
        elif sun[1] //step % 5 == 3:
            cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[3],outline=colors[3],tag=sun[4])
        elif sun[1] //step % 5 == 4:
            cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[4],outline=colors[4],tag=sun[4])
    # 判断边界方向
    if sun[0] >= 800 - sun[2]:
        sun[3] = 'Left'
    elif sun[0] <= 0:
        sun[3] = 'Right'
    elif sun[1] >= 600 - sun[2]:
        sun[3] = 'Up'
    elif sun[1] <= 0:
        sun[3] = 'Down' 


while True:
    # 控制小球移动，调用step_action函数
    step_action()
    time.sleep(0.1)
    window.update()


# 显示窗体
window.mainloop()

