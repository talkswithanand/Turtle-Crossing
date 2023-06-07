from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()



    def player_creation(self):
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.starting_position()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def starting_position(self):
        self.goto(STARTING_POSITION)

    def is_on_top(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

