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
        #To be able to compare your current score to the saved high score I use the open method to read the txt file 
        #The txt file is saved as a string so I convert it to an integer and set the value to the high_score attribute
        with open("data.txt", "r") as f_handle:
            high_score = f_handle.read()
            self.high_score = int(high_score)

        
        self.write(f"Score: {self.score} - High Score: {self.high_score}", align="center",font=("calibri", 20, "normal"))

        
    def update_scoreboard(self):
         """
         in the main.py file we call this method- if the head comes into contact with food it clears the screen (clearing the old score )
         , then re-writes the new updated score to be be displayed
         """
         self.clear()
         
         self.write(f"Score: {self.score} - High Score: {self.high_score}", align="center",font=("calibri", 20, "normal"))


    def add_one(self):
        """
        this method adds 1 point to your current score
        """
        self.score += 1
        self.update_scoreboard()
        


    def high_score_reset(self):
         """
         this method is called each time the snake eats. It's meant to update the high_score attribute the second a new high_score is achieved.
         """
         if self.score > self.high_score:
            self.high_score = self.score
            self.update_scoreboard()
         


    def reset(self):
        """
        This method controls the display values of the current score/game and the high score thats been saved.
        Along with resetting the score to 0 after a wall collision. 
        If your current score is higher than the saved high score then the value of the score attribute is transferred to the high_score attribute.
        This method also calls the update scoreboard method, which clears the previous written score and rewrites the current score effectively
        keeping the score constantly updated.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as f_handle:
                f_handle.write(str(self.high_score))
        self.update_scoreboard()
        
    #WORKS!!!!
    """ def write_score(self):
        
        This method controls what is written and saved as the high score along with reading what the current high score is.
        When this method is called the data.txt file is opened and read then converted to an integer form.
        With it now being converted it is then compared to the players current score.
        If the current score is higher than the saved score the open method reopens the data.txt file in write mode 
        converts the value to string form and writes that current score as the new high score 
        """
    """with open("data.txt", "r") as f_handle:
            score_data = f_handle.read()
            converted_data = int(score_data)
        if self.high_score > converted_data:
            with open("data.txt", "w") as f_handle:
                f_handle.write(str(self.high_score))"""
