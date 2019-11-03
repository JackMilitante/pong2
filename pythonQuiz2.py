import turtle
# Simple thing in Python3

wn = turtle.Screen()
wn.title("turtle quiz")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


wn.setup(width=600, height=600)





# square
square = turtle.Turtle()
square.shape("square")
square.color("red")
square.penup()
square.goto(-270, 0)

# triangle
triangle = turtle.Turtle()
triangle.shape("triangle")
triangle.color("blue")
triangle.penup()
triangle.goto(-140, 0)

# circle
circle = turtle.Turtle()
circle.shape("circle")
circle.color("yellow")
circle.penup()
circle.goto(140, 0)






#Main game loop
while True:
    wn.update()