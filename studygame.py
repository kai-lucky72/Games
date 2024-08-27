import turtle

wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.bgcolor("orange")
wn.title("ping pong")
wn.tracer(0)
score_a=0
score_b=0


pen = turtle.Turtle()
pen.hideturtle()
pen.color("blue")
pen.penup()
pen.sety(190)
pen.write("Player A: 0 Player B: 0", align="center", font=("courier",24,"normal"))

# stick_a
stick_b = turtle.Turtle()
stick_b.shape("square")
stick_b.color("violet")
stick_b.penup()
stick_b.shapesize(stretch_wid=10, stretch_len=1)
stick_b.goto(350, 0)
stick_b.speed(0)


# stick_
stick_a = turtle.Turtle()
stick_a.shape("square")
stick_a.color("violet")
stick_a.penup()
stick_a.shapesize(stretch_wid=10, stretch_len=1)
stick_a.goto(-350, 0)
stick_a.speed(0)


# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.speed(0)
ball.goto(0, 0)
ball.penup()
ball_dx = 0.1
ball_dy = 0.1


def stick_b_up():
    y = stick_b.ycor()
    y += 20
    stick_b.sety(y)


def stick_b_down():
    y = stick_b.ycor()
    y -= 20
    stick_b.sety(y)


def stick_a_up():
    y = stick_a.ycor()
    y += 20
    stick_a.sety(y)


def stick_a_down():
    y = stick_a.ycor()
    y -= 20
    stick_a.sety(y)


wn.listen()
wn.onkeypress(stick_a_up, "w")
wn.onkeypress(stick_a_down, "s")
wn.onkeypress(stick_b_up, "Up")
wn.onkeypress(stick_b_down, "Down")

while True:
    wn.update()

    ball.sety(ball.ycor() + ball_dy)
    ball.setx(ball.xcor() + ball_dx)

    if ball.ycor() > 280:
        ball.sety(280)
        ball_dy = -0.1
    if ball.ycor() < -280:
        ball.sety(-280)
        ball_dy = 0.1
    if ball.xcor() > 390:
        ball.setx(390)
        ball_dx = -0.1
        pen.clear()
        score_b +=1
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.setx(-390)
        ball_dx = 0.1
        score_a +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < stick_b.ycor() + 90 and ball.ycor() > stick_b.ycor() - 90):
        ball.setx(340)
        ball_dx = -0.1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < stick_a.ycor() + 90 and ball.ycor() > stick_a.ycor() - 90):
        ball.setx(-340)
        ball_dx = 0.1