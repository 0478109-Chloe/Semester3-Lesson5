# homework: in class, we drew a canvas with a bunch of carrots, potatos, and a sun.
# TODO: An incomplete version of a house has been added to the canvas. Edit the part where it draws the house, and reposition each piece so that the house is complete.
# website to run turtle is https://pyroom.app

import turtle
import random

# ---------- Setup ----------
t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.speed(0) # speed 0 is the fastest
t.pensize(1)
t.pencolor("green")
t.fillcolor("green")
screen.bgcolor("skyblue")
screen.setup(1000, 500) 

# we are going to draw a beautiful garden today

# ground
t.goto(-500, 50)
t.begin_fill()
for i in range(4):
    t.forward(1000)
    t.right(90)
t.end_fill()


t.goto(0, 0)


# one carrot:
def draw_carrot():
    t.pencolor("black")
    t.fillcolor("orange")
    t.begin_fill()
    t.forward(30)
    t.right(100)
    t.forward(80)
    t.right(160)
    t.forward(80)
    t.end_fill()

    t.pensize(10)
    t.pencolor("lime")
    t.forward(30)
    t.forward(-30)
    t.setheading(0)
    t.forward(30)
    t.left(75)
    t.forward(30)
    t.setheading(0)
    t.pensize(1)

def teleport(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# draw 10 carrots in random spots each run
for i in range(10):
    teleport(random.randint(-460, 460), random.randint(-170, 40))
    draw_carrot()


def draw_potato():
    t.pencolor("ivory")
    t.fillcolor("goldenrod")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

# draw 10 potatos in random spots each run
for i in range(10):
    teleport(random.randint(-460, 460), random.randint(-210, 10))
    draw_potato()


teleport(485, 165)

# sun
t.pencolor("yellow")
t.fillcolor("yellow")
t.pensize(10)

t.begin_fill()
for i in range(12):
    t.forward(42)
    t.left(30)
    # the lines (rays)
    t.right(105)
    t.forward(70)
    t.forward(-70)
    t.left(105)
t.end_fill()


teleport(0, 0)
t.pencolor("black")
t.pensize(2)

# house:
def draw_house():
    t.fillcolor("orange")
    t.begin_fill()
    for i in range(2):
        t.forward(170)
        t.left(90)
        t.forward(130)
        t.left(90)
    t.end_fill()

# window:
def draw_window():
    t.fillcolor("lightblue")
    t.begin_fill()
    for i in range(2):
        t.forward(40)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()

# roof:
def draw_roof():
    t.fillcolor("brown")
    t.begin_fill()
    t.forward(200)
    t.left(160)
    t.forward(106)
    t.left(40)
    t.forward(106)
    t.left(160)
    t.end_fill()

# TODO: edit the coordinates of this part, so that the house is neatly positioned.
teleport(0, 0)
draw_house()

teleport(25, 40)
draw_window()

teleport(-15, 130)
draw_roof()
