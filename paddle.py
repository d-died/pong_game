from turtle import Turtle

LEFT_PADDLE_COORDS = [(-370, 20), (-370, 0), (-370, -20)]
RIGHT_PADDLE_COORDS = [(370, 20), (370, 0), (370, -20)]


class Paddle:
    def __init__(self):
        self.left_paddle = []
        self.right_paddle = []
        self.make_paddle(paddle=self.left_paddle, positions=LEFT_PADDLE_COORDS)
        self.make_paddle(paddle=self.right_paddle, positions=RIGHT_PADDLE_COORDS)


    def make_paddle(self, paddle, positions):
        for position in positions:
            paddle_piece = Turtle("square")
            paddle_piece.color("white")
            paddle_piece.penup()
            paddle_piece.goto(position)
            paddle.append(paddle_piece)
        # print(paddle)

    def up(self, paddle_side):
        for i in range(3):
            square = paddle_side[i]
            print(f"Old y: {square.ycor()}")
            new_y = square.ycor() + 10
            paddle_side[i].goto(square.xcor(), new_y)
            print(f"New y: {square.ycor()}")
