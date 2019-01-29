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
# # 画小球模型
# cvs.create_oval(300,300,350,350,fill='red',outline='red',tag='sun')

sun = [300,300,50,'Right','SUN']
colors = ['red','yellow','blue','black','green']
# 画小球模型
cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[0],outline=colors[0],tag=sun[4])

def call_back(event):
    newx = event.x - sun[2]/2
    newy = event.y - sun[2]/2
    if newx % 5 == 0:
        cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[0],outline=colors[0],tag=sun[4])
    elif newx % 5 == 1:
        cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[1],outline=colors[1],tag=sun[4])
    elif newx % 5 == 2:
        cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[2],outline=colors[2],tag=sun[4])
    elif newx % 5 == 3:
        cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[3],outline=colors[3],tag=sun[4])
    elif newx % 5 == 4:
        cvs.create_oval(sun[0],sun[1],sun[0]+sun[2],sun[1]+sun[2],fill=colors[4],outline=colors[4],tag=sun[4])
    cvs.move('SUN',newx-sun[0],newy-sun[1])
    sun[0] = newx
    sun[1] = newy
    
    print(event.x,event.y)
    print(sun)
    

cvs.bind('<Motion>',call_back)

# 显示窗体
window.mainloop()

