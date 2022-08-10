from turtle import Turtle
from playsound import playsound 

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.hideturtle()
        self.penup()
        self.sety(275)
        self.color("#fff")
        self.write(f"Score: {self.score} Highest score: {self.highest_score}", font=("Courier", 24, "normal"), align="center")

    def increase_score(self):
        """Increases the score by 1 and prints new score."""
        playsound("../sound/score_sound.mp3", block=False)
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} Highest score: {self.highest_score}", font=("Courier", 24, "normal"), align="center")
        

    # def game_over(self):
    #     """Writes 'GAME OVER' on the screen."""
    #     playsound("../sound/game_over_sound.mp3", block=False)
    #     self.goto(0, 0)
    #     self.write("GAME OVER", font=("Courier", 24, "normal"), align="center")

    def reset(self):
        """Restarts the game, when the snake hits the wall or its tail"""
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} Highest score: {self.highest_score}", font=("Courier", 24, "normal"), align="center")