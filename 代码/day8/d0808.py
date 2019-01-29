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

sun = [300,300,50,'Right','sun']
# 画小球模型
cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill='red',outline='red',tag=sun[4])

def listener(event):
    if event.keysym =='Up':
        cvs.move('sun',0,-3)
        print(sun)
        sun[1] -= 3
    elif event.keysym == 'Down':
        cvs.move('sun',0,3)
        print(sun)
        sun[1] += 3
    elif event.keysym == 'Left':
        cvs.move('sun',-3,0)
        print(sun)
        sun[0] -= 3
    elif event.keysym == 'Right':
        cvs.move('sun',3,0)
        print(sun)
        sun[0] += 3
    print(sun)
# 安装监听器，调用listener函数
window.bind('<Key>',listener)


# def step_action():
#     step = 40
#     # 判断边界方向
#     if sun[0] >= 800 - sun[2]:
#         sun[3] = 'Left'
#     elif sun[0] <= 0:
#         sun[3] = 'Right'
#     elif sun[1] >= 600 - sun[2]:
#         sun[3] = 'Up'
#     elif sun[1] <= 0:
#         sun[3] = 'Down' 


# while True:
#     # 控制小球移动，调用step_action函数
#     step_action()
#     time.sleep(0.1)
#     window.update()
#     print(sun)


# 显示窗体
window.mainloop()

