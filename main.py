#Dragon-Drawing-Thingy-
#I'm too lazy to add in a description, oops, I just did, well, um, now I'm too lazy to delete it.

import turtle
bob = turtle.Turtle()
s = turtle.Screen()
leg = 0
square_rotation = 0
eye = 0
spikes = 0
tail_curve = 0


#Jim's body
bob.color("red")
bob.begin_fill()
bob.forward(300)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(600)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(300)
bob.end_fill()

#Jim's Legs and Shoes
bob.backward(240)
leg = 0

#loop that draws 4 legs
while leg < 4:
    leg += 1
    bob.begin_fill()
    bob.right(90)
    bob.forward(150)
    bob.left(90)
    bob.forward(30)
    bob.left(90)
    bob.forward(150)
    bob.end_fill()
    bob.backward(150)
    bob.right(90)
    bob.backward(30)
    bob.color("black")
    bob.begin_fill()
    bob.forward(60)
    bob.left(90)
    bob.forward(30)
    bob.left(90)
    bob.forward(60)
    bob.left(90)
    bob.forward(30)
    bob.end_fill()
    bob.left(90)
    bob.forward(30)
    bob.left(90)
    bob.forward(30)
    bob.color("red")
    bob.forward(120)
    bob.right(90)
    if leg < 4:
        bob.forward(120)

#Moving turtle to dragon's head
bob.forward(60)
bob.left(90)
bob.forward(100)
bob.right(90)
bob.forward(10)
bob.left(90)

#dragon head
bob.begin_fill()
bob.forward(90)
bob.left(90)
bob.forward(90)
bob.left(90)
bob.forward(90)
bob.end_fill()

#Moves turtle to dragon's eyes
bob.left(90)
bob.forward(15)
bob.left(90)
bob.forward(45)

#Create eyes
while eye < 2:
    eye += 1
    bob.color("white")
    bob.begin_fill()
    while square_rotation < 3:
        square_rotation += 1
        bob.forward(25)
        bob.right(90)
    square_rotation = 0
    bob.forward(25)
    bob.end_fill()
    bob.backward(5)
    bob.right(90)
    bob.forward(5)
    bob.color("black")
    bob.begin_fill()
    while square_rotation < 3:
        square_rotation += 1
        bob.forward(15)
        bob.right(90)
    square_rotation = 0
    bob.forward(15)
    bob.end_fill()
    if eye == 1:
        bob.color("white")
        bob.left(90)
        bob.forward(5)
        bob.left(90)
        bob.forward(20)
        bob.color("red")
        bob.forward(15)
        bob.left(90)
#move bob to head
bob.right(90)
bob.forward(15)
bob.color("white")
bob.forward(5)
bob.color("red")
bob.forward(20)

#draws horns
bob.color("orange")
bob.begin_fill()
bob.right(12)
bob.forward(41)
bob.right(156)
bob.forward(41)
bob.end_fill()
bob.right(102)
bob.forward(57)
bob.begin_fill()
bob.right(102)
bob.forward(41)
bob.right(156)
bob.forward(41)
bob.end_fill()

#Moving to spikes
bob.right(102)
bob.forward(17)
bob.color("red")
bob.forward(20)
bob.left(90)
bob.forward(90)
bob.right(90)

#Drawing spikes
while spikes < 17:
    spikes += 1
    bob.color("orange")
    bob.begin_fill()
    bob.forward(10)
    bob.right(60)
    bob.forward(20)
    bob.left(120)
    bob.forward(20)
    bob.end_fill()
    bob.right(60)

#Move to tail
bob.forward(10)
bob.left(90)
bob.forward(25)
bob.right(120)

#draw tail
while tail_curve < 100:
    tail_curve += 1
    bob.forward(1)
    bob.left(0.7)


s.exitonclick()
