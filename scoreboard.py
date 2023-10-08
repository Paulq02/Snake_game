#We're importing the turtle module since we've created a scoreboard class which will inheret everything from the Turtle module
from turtle import Turtle

#We initialize the super class along with some attributes - We created a turtle object to write some text along with the score attribute set at 0 
#We also tell the turtle to go to the top of the screen at Y-axis (370) and to have white text
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 370)
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score}", align="center",font=("calibri", 20, "normal"))

    def add_one(self):
        """
        in the main.py file we call this method- if the head comes into contact with food it clears the screen (clearing the old score )
        Then adds 1 to the score, then re-writes the new updated score to be be displayed
        """
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center",font=("calibri", 20, "normal"))

    def game_over(self):
        """
        This method is called in the main.py file - if the head comes into contact with any of the walls - the screen is cleared,
        The turtle goes to position (0, 0) and and GAME OVER text is written - alerting the user the game has ended
        
        """
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center",font=("calibri", 20, "normal"))
