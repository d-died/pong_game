from turtle import Turtle

PADDLE_COORDS = [(-350, 0), (350, 0)]

class Paddle:
    def __init__(self):
        self.left_paddle = None
        self.right_paddle = None
        self.make_paddle()


    def make_paddle(self):
        for i in range(len(PADDLE_COORDS)):
            paddle = Turtle("square")
            paddle.resizemode("user")
            paddle.color("white")
            paddle.setheading(90)
            paddle.shapesize(stretch_len=7.5)
            paddle.penup()
            paddle.goto(PADDLE_COORDS[i])
            print(paddle)
            if PADDLE_COORDS[i] == (-350, 0):
                self.left_paddle = paddle
            else:
                self.right_paddle = paddle


    def left_up(self):
        old_y = self.left_paddle.ycor()
        if old_y <= 200:
            new_y = old_y + 20
            self.left_paddle.sety(new_y)

    def left_down(self):
        old_y = self.left_paddle.ycor()
        if old_y >= -200:
            new_y = old_y - 20
            self.left_paddle.sety(new_y)

    def right_up(self):
        old_y = self.right_paddle.ycor()
        if old_y <= 200:
            new_y = old_y + 20
            self.right_paddle.sety(new_y)

    def right_down(self):
        old_y = self.right_paddle.ycor()
        if old_y >= -200:
            new_y = old_y - 20
            self.right_paddle.sety(new_y)
