from turtle import *

# bite(x,y) coordinates
def bite(x ,y):
    speed(100)
    
    up()
    color("black")
    goto(x,y)
    down()
    
    fillcolor("black")
    begin_fill()
    circle(30)
    end_fill()
    
    up()
    goto(x+50,y)
    down()
    
    begin_fill()
    circle(30)
    end_fill()
    
    up()
    goto(x,y)
    right(90)
    down()
    
    begin_fill()
    fd(120)
    left(90)
    fd(50)
    left(90)
    fd(145)
    left(90)
    fd(50)
    left(90)
    fd(25)
    end_fill()
    
    up()
    color("pink")
    fd(120)
    down()
    
    fillcolor("pink")
    begin_fill()
    circle(25,180)
    left(90)
    fd(25)
    end_fill()
    
    up()
    left(90)
    fd(15)
    down()
    
    color("white")
    fd(10)
    
    speed(2)
    color("yellow")
    circle(70,100)
    
    done()