from turtle import Turtle
from random import randint



class Food(Turtle):
    """
    When a food object is created a turtle is created and displayed in a random location on the screen, given the random number generated for the x,y
    coordinates - turtle object is a red circle shrank to increase game difficulty
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("red")
        random_x =  randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
        
        
       
    def refresh_food(self):
        """
        This method is called when the head comes into contact with the food - a new random x,y number/coordinate is generated and displayed to 
        a random location on the screen
        """
        random_x =  randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)

        
    

