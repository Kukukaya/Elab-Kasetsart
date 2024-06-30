import turtle
from turtlelab4 import check

def draw_square(size):
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)

def draw_triangle(size):
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    
turtle.left(30)
draw_square(120)
turtle.right(90)
turtle.forward(120)
turtle.right(90)
draw_triangle(120)
check()