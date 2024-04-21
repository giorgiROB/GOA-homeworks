
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

penup()
goto(300,300)
pendown()
color("blue")
begin_fill()
forward(90)
right(90)
forward(35)
right(90)
forward(90)
right(90)
forward(35)
end_fill()


#home
color("brown")
right(90)
forward(90)
right(90)
forward(35)
left(90)
forward(220)
left(90)
forward(220)
left(90)
forward(220)
left(90)
forward(220)

color("green")
begin_fill()
right(180)
forward(35)
left(60)
forward(185)
right(120)
forward(185)
end_fill()

color("purple")
begin_fill()
right(30)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
end_fill()
penup()
goto(265,210)
pendown()
begin_fill()
forward(45)
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
end_fill()


#door
right(180)
color("brown")
forward(220)
left(90)
forward(80)
left(90)
color("yellow")
begin_fill()
forward(130)
right(90)
forward(70)
right(90)
forward(130)
end_fill()

#tree
penup()
goto(-200,-50)
pendown()
color("brown")
begin_fill()
right(90)
forward(50)
right(90)
forward(250)
right(90)
forward(50)
right(90)
forward(250)
end_fill()
left(180)
forward(250)
color("green")
begin_fill()
right(90)
forward(100)
left(90)
forward(150)
left(90)
forward(240)
left(90)
forward(150)
left(90)
forward(90)
end_fill()


exitonclick()
























