from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("The Pong Game")
screen.tracer(0)

paddle = Paddle()
left = paddle.left_paddle
right = paddle.right_paddle
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
screen.onkey(paddle.up(left), "Up")
screen.update()

# paddle.up(paddle.left_paddle)


screen.exitonclick()