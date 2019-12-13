import turtle
from random import choice,randint

window = turtle.Screen()
window.title("Ping-Pongg")
window.setup(width=1.0 ,height=1.0)
window.bgcolor("gray")
window.tracer(2)

border = turtle.Turtle()
border.speed(0)
border.color('purple')
border.begin_fill()
border.goto(-500,300)
border.goto(500,300)
border.goto(500,-300)
border.goto(-500,-300)
border.goto(-500,300)
border.end_fill()

border.goto(0,300)
border.color('white')
border.setheading(270)
for i in range(25):
    if i&1==0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

rocket_1 = turtle.Turtle()
rocket_1.color('white')
rocket_1.shape('square')
rocket_1.shapesize(stretch_len=1, stretch_wid=8)
rocket_1.penup()
rocket_1.goto(-450,0)

def move_up():
    y = rocket_1.ycor() + 15
    if y > 240:
        y = 240
    rocket_1.sety(y)

def move_down():
    y = rocket_1.ycor() - 15
    if y < -240:
        y = -240
    rocket_1.sety(y)

window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")

rocket_2 = turtle.Turtle()
rocket_2.color('white')
rocket_2.shape('square')
rocket_2.shapesize(stretch_len=1, stretch_wid=8)
rocket_2.penup()
rocket_2.goto(450,0)

FONT = ("Arial", 45)
score_a = 0
s1 = turtle.Turtle(visible= False)
s1.color('white')
s1.penup()
s1.setposition(-200,300)
s1.write(score_a,font = FONT)

score_b = 0
s2 = turtle.Turtle(visible= False)
s2.color('white')
s2.penup()
s2.setposition(200,300)
s2.write(score_a,font = FONT)

def move_up():
    y = rocket_2.ycor() + 15
    if y > 240:
        y = 240
    rocket_2.sety(y)

def move_down():
    y = rocket_2.ycor() - 15
    if y < -240:
        y = -240
    rocket_2.sety(y)

ball = turtle.Turtle()
ball.shape('circle')
ball.speed(1)
ball.color('black')
ball.dx = 2
ball.dy = -2
ball.penup()

window.listen()
window.onkeypress(move_up, "r")
window.onkeypress(move_down, "f")

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() <= -490:
        score_a += 1
        s2.clear()
        s2.write(score_a, font=FONT)
        ball.goto(0,randint(-150,150))
        ball.dx = choice([-4,-3,-2, 2,3,4])
        ball.dy = choice([-4,-3,-2, 2,3,4])

    if ball.xcor() >= 490:
        score_b += 1
        s1.clear()
        s1.write(score_b, font = FONT)
        ball.goto(0, randint(-150,150))
        ball.dx = choice([-4,-3,-2, 2,3,4])
        ball.dy = choice([-4,-3,-2, 2,3,4])


    if ball.ycor() >= rocket_2.ycor()-50 and ball.ycor() <= rocket_2.ycor()+50 \
        and ball.xcor() >= rocket_2.xcor()-5 and ball.xcor() <= rocket_2.xcor()+5:
        ball.dx = -ball.dx

    if ball.ycor() >= rocket_1.ycor()-50 and ball.ycor() <= rocket_1.ycor()+50 \
        and ball.xcor() >= rocket_1.xcor()-5 and ball.xcor() <= rocket_1.xcor()+5:
        ball.dx = -ball.dx


window.mainloop()