import turtle
import time
myPen=turtle.Pen()
myPen.speed(0)
myPen.pensize(5)
circle_pos=[(0,0),(100,0),(50,-55),(-50,-55),(-100,0)]
colors=["black","red","green","yellow","blue"]
continent_name=["非洲","美洲","大洋洲","亚洲","欧洲"]
continent_pos=[(0,0+50),(100,0+50),(50,-55+50),(-50,-55+50),(-100,0+50)]
for i in range(5):
    myPen.penup()
    myPen.goto(circle_pos[i])
    myPen.pendown()
    myPen.pencolor(colors[i])
    myPen.circle(50)
    myPen.penup()
    myPen.goto(continent_pos[i])
    myPen.pendown()
    myPen.write(continent_name[i],font=("Arical",13))
time.sleep(60)
turtle.done