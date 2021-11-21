import turtle
import draw_USA_flag
import drawCircle
import print_me_first

"""
This program will draw a USA flag on the screen and an USA map as backgroun
A tiltl "USA OLYMPIC TEAM" will be drew on top of the flag, and a Olympic ring
will be drew below the flag. Also, Auther's name, program name, and current time
will be printed on the right bottom corner 
"""

def main():

#------ create a screen------
    screen = turtle.getscreen()
        # set background color of screen
    screen.bgcolor("white")
        # set tile of screen
    screen.title("USA Flag - https://www.pythoncircle.com")
        # set usa map as background
    turtle.bgpic("usa.png")

#------drawing------
        # write "USA OLYMPIC TEAM" on top 
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,300)
    turtle.pendown()
    turtle.pencolor("blue")
    turtle.write("USA OLYMPIC TEAM", align = 'center', font = (" ",40,'bold'))

        # draw USA flag
    draw_USA_flag.draw_USA_flag()
    color = ['blue','orange','black','green','red']# a list of color of olympic rings
    count = 0   # a counter variable
    x = -180    # starting x value of the first ring
    y = -300    # statting y value of the first ring
    for count in range(5):   # A loop of drawing 5 rings
        drawCircle.drawCircle(x,y,color[count])
        x += 87.5
        if y == -300:
            y -= 70
        else :
            y = -300
        count +=1

        # print authoer's info on screen
    info = print_me_first.print_first("Ziwen Li")
    turtle.penup()
    turtle.goto(300,-350)
    turtle.pencolor('blue')
    turtle.write(info)
 
    screen.mainloop()   # keep holding the screen until closed manually

if __name__ == "__main__":
    main()
