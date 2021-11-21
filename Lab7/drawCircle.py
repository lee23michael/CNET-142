import turtle


def drawCircle(x,y,color):

    RADIUS = 70
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.speed(9999)
    turtle.pencolor(color) 
    turtle.penup() # when penup is set, drawing is disabled when move the cursor
    turtle.goto(x, y) # move the cursor to (x, y)
    turtle.pendown() #when pendown is setup, drawing is enabled
    turtle.circle(RADIUS) # draw a circle
    





#drawCircle(-180,-300,'blue')
#drawCircle(-110,-370,'blue')
#drawCircle(-40,-300,'blue')
#drawCircle(30,-370,'blue')
#drawCircle(70,-300,'blue')