import turtle
def draw():
    turtle.pensize(1)
    turtle.bgcolor('black')
    colors = ['red','yellow','blue','green']
    turtle.speed(10)
    for x in range(400):
        turtle.forward(2*x)
        turtle.color(colors[x%4])
        turtle.left(91)
    turtle.mainloop()

# 程序执行入口
if __name__ == '__main__':
    draw()