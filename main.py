from turtle import Turtle, Screen
from paddle import Paddle
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("The Pong Game")
screen.tracer(0)

paddle = Paddle()
# left = paddle.left_paddle
# right = paddle.right_paddle
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

screen.listen()
screen.onkey(paddle.left_up, "Up")
screen.onkey(paddle.left_down, "Down")
screen.onkey(paddle.right_up, "w")
screen.onkey(paddle.right_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)



# paddle.up(paddle.left_paddle)


screen.exitonclick()