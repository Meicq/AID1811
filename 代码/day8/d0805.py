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
# 画小球模型
cvs.create_oval(300,300,350,350,fill='red',outline='red',tag='sun')

def listener(event):
    if event.keysym =='Up':
        cvs.move('sun',0,-3)
    elif event.keysym == 'Down':
        cvs.move('sun',0,3)
    elif event.keysym == 'Left':
        cvs.move('sun',-3,0)
    elif event.keysym == 'Right':
        cvs.move('sun',3,0)


# 安装监听器
window.bind('<Key>',listener)

# 显示窗体
window.mainloop()

