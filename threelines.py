# SAM MARTORANA

# ################################ [H2_1] ################################# #
# Write a program draws the picture within the box (but you don't need to
# draw the box.) Each line is of length 200 and separated from the next line
# by 30 units. The bottom right end of the lowest line is at (0,0) (the
# turtle's home location), and all lines have a pen width of 3. (HTT4 has a
# code example that shows how to set the pen width for a turtle.) Be sure to
# have wn.exitonclick() as the last statement of your program.
# ########################################################################## #

import turtle

wn = turtle.Screen()

dave = turtle.Turtle()

dave.width(3)

def makeLines(length):
    dave.pendown()
    dave.forward(length)
    dave.penup()


dave.right(180)

makeLines(200)
dave.right(90)
dave.forward(30)
dave.right(90)

makeLines(200)
dave.left(90)
dave.forward(30)
dave.left(90)

makeLines(200)



wn.exitonclick()