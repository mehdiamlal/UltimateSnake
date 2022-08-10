from turtle import Turtle
from playsound import playsound 

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = self.retrieve_highest_score()
        self.hideturtle()
        self.penup()
        self.sety(275)
        self.color("#fff")
        self.write(f"Score: {self.score} Highest score: {self.highest_score}", font=("Courier", 24, "normal"), align="center")
    
    def update_score_data(self):
        """Updates the .txt file with the new highest score."""
        with open("score_data.txt", mode="w") as file:
            file.write(f"{self.highest_score}")

    def retrieve_highest_score(self):
        """Retrieves the highest score when a new instance of the game is run."""
        with open("score_data.txt") as file:
            data = file.read() 
            if len(data) == 0:
                return 0
            else:
                print(data)
                return int(data)


    def increase_score(self):
        """Increases the score by 1 and prints new score."""
        playsound("../sound/score_sound.mp3", block=False)
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} Highest score: {self.highest_score}", font=("Courier", 24, "normal"), align="center")
        

    def reset(self):
        """Restarts the game, when the snake hits the wall or its tail"""
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.update_score_data()
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} Highest score: {self.highest_score}", font=("Courier", 24, "normal"), align="center")