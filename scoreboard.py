from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.penup()
        self.goto(0, 240)
        self.color("white")
        self.hideturtle()
        self.write(f"{self.left_score}  {self.right_score}", align=ALIGNMENT, font=FONT)

    def add_point(self, player):
        if player == "right":
            self.right_score += 1
            print(self.right_score)
        else:
            self.left_score += 1
            print(self.left_score)
        self.clear()
        self.write(f"{self.left_score}  {self.right_score}", align=ALIGNMENT, font=FONT)