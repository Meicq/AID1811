# tkinter
import tkinter as tk
# 创建窗体对象
window = tk.Tk() # 工具是大写的T,小写的k
# 设置窗体标题
window.title('球球大作战')
# 设置窗体大小
window.geometry('1024x768+0+0') # x是字母x,1024x768是屏幕分辨率,第一个+0是值屏幕的+x坐标,第二个+0是+y坐标
# 创建画布对象
# 颜色代码,red,yellow,bule,...
# RGB三原色　   00~FF   #ABCDEF
cvs = tk.Canvas(window,bg='#ABCDEF')
# 画布包装在窗体上(expand=tk.TES让画布居中,fill=tk.BOTH让画布充满整个屏幕)
cvs.pack(expand=tk.YES,fill=tk.BOTH)
# --------------------------------------------------------
cvs.create_oval(300,300,350,350,fill='red',outline='red',tag='sun')
import time
# for x in range(100):
while True:
    cvs.move('sun',1,1)
    time.sleep(0.1) # 休眠
    window.update() # 窗口刷新

# --------------------------------------------------------
# 显示窗体
window.mainloop()