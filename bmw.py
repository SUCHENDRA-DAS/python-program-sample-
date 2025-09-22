import turtle
#Setup screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
#Create turtle
t = turtle.Turtle()
t.speed(5)
t.hideturtle()
#Outer black circle
t.penup()
t.goto(0, -150)
t.pendown()
t.pensize(5)
t.color("black", "white")
t.begin_fill()
t.circle(150)
t.end_fill()
#Draw 4 quadrants (lines)
t.pensize(2)
for angle in [0, 90]:
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.pendown()
    t.forward(150)
    t.backward(300)
    t.forward(150)
#Fill blue quadrants (top-right and bottom-left)
def fill_quadrant(start_angle):
    t.penup()
    t.goto(0, 0)
    t.setheading(start_angle)
    t.forward(148)
    t.setheading(start_angle + 90)
    t.begin_fill()
    t.fillcolor("blue")
    t.circle(148, 90)
    t.goto(0, 0)
    t.end_fill()
fill_quadrant(90) # Top-right
fill_quadrant(270) # Bottom-left
turtle.done()
