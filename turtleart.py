# SAM MARTORANA

# ################################ [H2_1] ################################# #
# Write an original program to draw some kind of picture using turtle
# graphics. Be creative and experiment with the turtle methods provided in
# HTT's Summary of Turtle Methods. Online exhaustive documentation of Turtle
# Graphics is here: https://docs.python.org/3/library/turtle.html.
# ########################################################################## #

import turtle

wn = turtle.Screen()

dave = turtle.Turtle()

def drawFrog():

    # body
    dave.fillcolor('green')
    dave.begin_fill()

    for i in range(3):
        dave.down()
        dave.forward(100)
        dave.circle(10, 120)

    dave.end_fill()

    # eyes
    dave.fillcolor('white')

    dave.penup()
    dave.goto(60, 60)
    dave.pendown()
    dave.begin_fill()
    dave.circle(10)
    dave.end_fill()
    dave.penup()
    dave.goto(40, 60)
    dave.pendown()
    dave.begin_fill()
    dave.circle(10)
    dave.end_fill()
    dave.penup()

    dave.fillcolor('black')
    dave.goto(60, 65)
    dave.pendown()
    dave.begin_fill()
    dave.circle(5)
    dave.end_fill()
    dave.penup()
    dave.goto(40, 65)
    dave.pendown()
    dave.begin_fill()
    dave.circle(5)
    dave.end_fill()

    # nostrils
    dave.penup()
    dave.goto(40, 50)
    dave.pendown()
    dave.forward(5)
    dave.penup()
    dave.forward(15)
    dave.pendown()
    dave.forward(5)

    #  front legs
    dave.penup()
    dave.goto(30, 30)
    dave.pendown()
    dave.right(90)
    dave.forward(30)
    dave.penup()

    dave.goto(40, 30)
    dave.pendown()
    dave.forward(30)
    dave.penup()

    dave.goto(60, 30)
    dave.pendown()
    dave.forward(30)
    dave.penup()

    dave.goto(70, 30)
    dave.pendown()
    dave.forward(30)
    dave.penup()

    dave.forward(30)
    dave.penup()

    # back legs
    dave.penup()
    dave.goto(10, 30)
    dave.pendown()
    dave.forward(15)
    dave.left(90)
    dave.forward(5)
    dave.right(90)
    dave.forward(15)
    dave.penup()

    dave.goto(90, 30)
    dave.pendown()
    dave.forward(15)
    dave.right(90)
    dave.forward(5)
    dave.left(90)
    dave.forward(15)
    dave.penup()

    dave.goto(-200, -200)


drawFrog()

wn.exitonclick()