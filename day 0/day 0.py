from turtle import *


#we want to paint house

#step 1: draw a square
speed(30)
color("green")
width(7)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
#end of drawing a square 

#step 2: draw a door

left(90)
forward(70)
color("red")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()


color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#step 3: make a windows
left(60)
right(30)
color("purple")
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(50)

penup()
goto(200,200)
pendown()

forward(50)
left(90)
left(180)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(50)
right(90)
forward(25)
left(90)
left(90)
forward(50)
left(90)
forward(50)


#step idk: draw a chimney
color("brown")
begin_fill()
forward(130)
left(90)
forward(50)
left(90)
forward(50)
end_fill()



