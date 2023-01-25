import turtle
t=turtle.Turtle()
s=turtle.Screen()
turtle.bgcolor('black')
t.width(2)
t.speed(15)

col = ("green","white","red")
for i in range (250):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)