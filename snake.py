from turtle import Turtle, Screen
from food import Food

#This list of tuples are the starting positions of the 3 turtles that make up the beginning snake
POSITIONS = [(0, 0 ), (-20, 0), (-40, 0)]

#The directional coordinate of left is 180
LEFT = 180

#The directional coordinate of right is 0
RIGHT = 0

#The directional coordinate of up is 90
UP = 90

#The directional coordinate of down is 270
DOWN = 270

class Snake:

    def __init__(self):
        """
        When a snake object is created an empty list is created called turtle cage which will hold the beginning 3 turtles representing the snake.
        The create_snake method is also called. Also the first turtle created at index position 0 is designated as the head of the snake
        """
        self.turtle_cage = []
        self.create_snake()
        self.head = self.turtle_cage[0]

    def create_snake(self):
        """
        When this method is called a for loop is run in the POSITIONS constant (the starting posistions/coordinates) of the 3 starting turtles -
        Along with the add_turtles method being called creating the turtles, shape, color and adding each turtle to the turtle_cage list
        """
        for turtle_position in POSITIONS:
            self.add_turtles(turtle_position)
            
    
    def add_turtles(self, turtle_position):
        """
        This method is used when creating a snake object - it creates the turtle along with its color, shape and position on the screen
        Takes argument from the create_snake method, getting the positions on where to go
        """
        new_turtle = Turtle()
        new_turtle.color("white")
        new_turtle.shape("square")
        new_turtle.penup()
        new_turtle.goto(turtle_position)
        self.turtle_cage.append(new_turtle)

    def extend_snake(self):
        """
        This method calls the add_turtles method - When the head comes into contact with the food, a turtle is created 
        and added to the END of the turtle_cage list by getting the position of the last turtle in the turtle_cage list hence the [-1]
        
        """
        self.add_turtles(self.turtle_cage[-1].position())
    
    
    

    def move(self):
        """
        This method is used to move the snake - it runs a for loop in the turtle_cage list with range of how long the turtle_cage list is, counting backwards 
        and stopping at 0 - It gets hold of the 2nd turtles x and y coordinates to give to the coordinates to the tail to follow - the head then moves forward
        by 20 the following loop the heads coordinates are taken and the body follows the head - essentially it links the turtles together moving 
        tail - to the body position, body - to the heads position, then finally the head moves - this repeats non-stop

        """
        for seg_num in range(len(self.turtle_cage)-1, 0, -1):
            new_x = self.turtle_cage[seg_num -1].xcor()
            new_y = self.turtle_cage[seg_num -1].ycor()
            self.turtle_cage[seg_num].goto(new_x, new_y)
        self.head.forward(20)


    def left(self):
        """
        Controls the movement of the snake head -
        If the head is pointing towards east (0) you will be unable to 
        press the left arrow key and go backwards
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Controls the movement of the snake head -
        If the head is pointing towards West (180) you will be unable to 
        press the right arrow key and go backwards
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        """
        Controls the movement of the snake head -
        If the head is pointing towards South (270) you will be unable to 
        press the up arrow key and go backwards
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Controls the movement of the snake head -
        If the head is pointing towards North (90) you will be unable to 
        press the Down arrow key and go backwards
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    
        
        

            


