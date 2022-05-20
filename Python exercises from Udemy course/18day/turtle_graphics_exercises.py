from turtle import Turtle, Screen
from random import randint

def turn_right_and_advance(angle_turn,advance,how_many_times) :
 i = 0
 while i < len(range(how_many_times)) :
  timmy_the_turtle.right(angle_turn) 
  timmy_the_turtle.forward(advance)
  i += 1

def draw_dashed_line(points,distance) :
 i = 0 
 while i < range(len(points)) :
  timmy_the_turtle.dot()
  timmy_the_turtle.penup()
  timmy_the_turtle.forward(distance)
  timmy_the_turtle.pendown()
  i += 1

def draw_equal_side(how_many_shapes,shape_size) :
 i = 0
 sides = 3
 while i < how_many_shapes :
  angles = 360 / sides
  timmy_the_turtle.pencolor(randint(1,255),randint(1,255),randint(1,255))
  turn_right_and_advance(angles,shape_size,sides)
  sides += 1
  i += 1

def random_walk(iteration,steps,angles) :
 for _ in range(iteration) :
  direction = randint(1,4)
  forward_backwared = randint(1,2)
  if direction == 1 : 
   timmy_the_turtle.pencolor(randint(1,255),randint(1,255),randint(1,255))
   timmy_the_turtle.forward(steps)
  elif direction == 2 :  
   timmy_the_turtle.pencolor(randint(1,255),randint(1,255),randint(1,255))
   timmy_the_turtle.backward(steps)
  elif direction == 3 :  
   timmy_the_turtle.pencolor(randint(1,255),randint(1,255),randint(1,255))
   timmy_the_turtle.right(angles)
   if forward_backwared == 1 :
    timmy_the_turtle.forward(steps) 
   else :
    timmy_the_turtle.backward(steps)
  else :  
   timmy_the_turtle.pencolor(randint(1,255),randint(1,255),randint(1,255))
   timmy_the_turtle.left(angles)
   if forward_backwared == 1 :
    timmy_the_turtle.forward(steps) 
   else :
    timmy_the_turtle.backward(steps)

def little_circle(steps) :
    timmy_the_turtle.penup()
    timmy_the_turtle.circle(0,360/steps)
    timmy_the_turtle.pendown()

def spirograph(radius,steps) :
    for _ in range(steps) :
        timmy_the_turtle.pencolor(randint(1,255),randint(1,255),randint(1,255))
        timmy_the_turtle.circle(radius)
        little_circle(steps)


screen = Screen()
screen.colormode(255)

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.pensize(2)
timmy_the_turtle.speed(0)

# #create square
# timmy_the_turtle.forward(100)
# turn_right_and_advance(90,100,3)
# draw_dashed_line(10,10)
# draw_equal_side(10,100)
# random_walk(20000,5,90)
# spirograph(100,50)

screen.exitonclick()