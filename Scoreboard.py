from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,267)
        self.update()

    def update(self):
        #UPDATE THE SCORE
        self.score += 1
        self.display()

    def display(self):
        #DISPLAY UPDATED SCORE
       self.clear()
       self.write(f"Score = {self.score}",align='center',font=("Ariel",20))

    def game_over(self):
        #WHEN THE GAME ENDS, DISPLAY THE SCORE
        self.clear()
        self.goto(0,0)
        self.write(f"GAMEOVER!!\nScore = {self.score}", align='center', font=("Ariel", 20))

