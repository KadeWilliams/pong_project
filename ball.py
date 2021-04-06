from turtle import Turtle

TOP_WALL = 280
BOTTOM_WALL = -280


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.move_speed = .1
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        if self.ycor() > TOP_WALL or self.ycor() < BOTTOM_WALL:
            self.bounce_y()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.move_speed *= .9
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = .1
        self.bounce_x()


