import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("The Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
# Drawing the middle line
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.pencolor("white")
tim.width(8)
tim.goto(0, 290)
tim.setheading(270)
tim.pendown()
for _ in range(580):
    tim.forward(30)
    tim.penup()
    tim.forward(20)
    tim.pendown()

# Creating a scoreboard:
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    elif ball.xcor() > 380:
        scoreboard.add_point("right")
        ball.start_over()
    elif ball.xcor() < -380:
        scoreboard.add_point("left")
        ball.start_over()
    ball.move()


screen.exitonclick()