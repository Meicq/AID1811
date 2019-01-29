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
# 画线(x1,y1,x2,y2)
cvs.create_line(20,20,300,20,width=3,fill='red')
# 画矩形(x1,y1,x2,y2)
cvs.create_rectangle(20,30,300,300,fill='red',outline='red')
# 画圆(x1,y1,x2,y2)
cvs.create_oval(20,400,300,450,fill='red',outline='red')
# 画文本
cvs.create_text(500,500,text='python',fill='red',font=('Arial',20))


# 显示窗体
window.mainloop()





#　图片格式
# .png  支持透明色
