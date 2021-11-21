import turtle
import draw_USA_flag
import drawCircle
import print_me_first

def main():

    # create a screen
    screen = turtle.getscreen()
        # set background color of screen
    screen.bgcolor("white")
        # set tile of screen
    screen.title("USA Flag - https://www.pythoncircle.com")
        # set usa map as background
    turtle.bgpic("usa.png")
        # Write "USA OLYMPIC TEAM" on top 
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,300)
    turtle.pendown()
    turtle.pencolor("blue")
    turtle.write("USA OLYMPIC TEAM", align = 'center', font = (" ",40,'bold'))
        # draw usa flag
    draw_USA_flag.draw_USA_flag()

        



        # a list of color of olympic rings
    color = ['blue','orange','black','green','red']

    count = 0   # a counter variable
    x = -180    # starting x value of the first ring
    y = -300    # statting y value of the first ring

        # A loop of drawing 5 rings
    for count in range(5) :
        drawCircle.drawCircle(x,y,color[count])
        x += 87.5
        if y == -300:
            y -= 70
        else :
            y = -300
        count +=1

        # print authoer info on screen
    info = print_me_first.print_first("Ziwen Li")
    turtle.penup()
    turtle.goto(300,-350)
    turtle.pencolor('blue')
    turtle.write(info)


    screen.mainloop()

if __name__ == "__main__":
    main()
