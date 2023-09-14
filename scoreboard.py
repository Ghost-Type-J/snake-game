from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(x=0, y=270)
        self.score_count = 0
        self.write(arg=f"Score: {self.score_count}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score_count}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def points_up(self):
        self.clear()
        self.score_count += 1
        self.update_scoreboard()
