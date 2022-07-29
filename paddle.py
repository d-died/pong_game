from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        old_y = self.ycor()
        if old_y <= 220:
            new_y = old_y + 20
            self.sety(new_y)

    def down(self):
        old_y = self.ycor()
        if old_y >= -220:
            new_y = old_y - 20
            self.sety(new_y)
