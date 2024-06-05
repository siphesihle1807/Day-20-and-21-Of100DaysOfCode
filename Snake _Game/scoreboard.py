from turtle import Turtle
ALIGNMEMT = "center"
FONT = ("Arial", 16, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # accounts for the writing on the screen
        self.score = 0
        self.up()
        self.goto(0, 270)
        self.ht()
        self.score_update()
        # self.end_game()


    def score_update(self):
        self.write(f"Score: {self.score}", align=ALIGNMEMT, font=FONT)

    def end_game(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMEMT, font=FONT)


    def score_increase(self):
        self.score += 1
        # clears previous text
        self.clear()
        self.score_update()