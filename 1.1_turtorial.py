'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
something

'''
import turtle
mando=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('white') # colors the screen
mando.pensize(3) # width of pen line
mando.speed(10)  # speed of drawing. Go fast to not waste time.
mando.penup()

mando.color("silver")
mando.begin_fill() #this section builds the helmet dome
mando.goto(0,-70)
mando.circle(130)
mando.end_fill()

mando.begin_fill()
mando.penup() #builds the right cheek
mando.goto(-140,25)
mando.pendown()
mando.goto(-140,-100)
mando.goto(-40,-130)
mando.goto(-10,-130)
mando.goto(-10,25)
mando.goto(-140,25)
mando.penup()
mando.end_fill()

mando.begin_fill()
mando.goto(140,25) #builds the left cheek
mando.pendown()
mando.goto(140,-100)
mando.goto(40,-130)
mando.goto(10,-130)
mando.goto(10,25)
mando.goto(140,25)
mando.penup()
mando.end_fill()

mando.color("darkgrey")
mando.begin_fill() #builds the right cheek insert
mando.goto(-120,5)
mando.pendown()
mando.goto(-120,-40)
mando.goto(-40,-100)
mando.goto(-40,5)
mando.goto(-120,5)
mando.penup()
mando.end_fill()

mando.begin_fill()
mando.goto(120,5) #builds the left cheek insert
mando.pendown()
mando.goto(120,-40)
mando.goto(40,-100)
mando.goto(40,5)
mando.goto(120,5)
mando.penup()
mando.end_fill()

mando.color("gainsboro")
mando.goto(-25,80) #builds the main body of the mowhawk
mando.pendown()
mando.begin_fill()
mando.goto(-25,185)
mando.goto(-10,200)
mando.goto(10,200)
mando.goto(25,185)
mando.goto(25,80)
mando.goto(10,65)
mando.goto(-10,65)
mando.goto(-25,80)
mando.end_fill()
mando.penup()

mando.color("lightsteelblue")
mando.goto(-10,200)
mando.pendown() #biulds the top of the mowhawk
mando.begin_fill()
mando.goto(10,200)
mando.goto(10,80)
mando.goto(5,75)
mando.goto(-5,75)
mando.goto(-10,80)
mando.goto(-10,200)
mando.penup()
mando.end_fill()

mando.color("black")
mando.goto(-140,50) #this section makes the visor
mando.begin_fill()
mando.pendown()
mando.goto(140,50)
mando.goto(140,25)
mando.goto(25,15)
mando.goto(20,-120)
mando.goto(30,-130)
mando.goto(-30,-130)
mando.goto(-20,-120)
mando.goto(-25,15)
mando.goto(-140,25)
mando.goto(-140,50)
mando.penup()
mando.end_fill()

mando.color("silver")
mando.goto(-140,50) #builds the visor shield
mando.begin_fill()
mando.pendown()
mando.goto(140,50)
mando.goto(140,60)
mando.goto(-140,60)
mando.goto(-140,50)
mando.penup()
mando.end_fill()

mando.goto(180,-190)
mando.color("crimson")
mando.write('Will Jacobson',font=("ironwood", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
