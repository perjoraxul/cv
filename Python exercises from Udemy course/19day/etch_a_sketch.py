from turtle import Turtle, Screen


def move_forwards() :
    radu.forward(10)

def move_backwards() :
    radu.backward(10)

def move_right() :
    radu.right(10)

def move_left() :
    radu.left(10)

def clear_window() :
    radu.clear()
    radu.penup()
    radu.home()
    radu.pendown()

radu = Turtle()

screen = Screen()



screen.listen()



screen.onkeypress(fun=move_forwards,key="w")
screen.onkeypress(fun=move_backwards,key="s")
screen.onkeypress(fun=move_right,key="d")
screen.onkeypress(fun=move_left,key="a")
screen.onkey(fun=clear_window,key="c")
screen.exitonclick()