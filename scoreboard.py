from turtle import Turtle


ALIGN = 'center'
FONT = ('Courier', 80, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 190)
        self.write(f"{self.left_score}", align=ALIGN, font=FONT)
        self.goto(100, 190)
        self.write(f"{self.right_score}", align=ALIGN, font=FONT)

    def right_increase(self):
        self.right_score += 1
        self.update_scoreboard()

    def left_increase(self):
        self.left_score += 1
        self.update_scoreboard()



