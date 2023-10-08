#turtle module is imported along with screen class
from turtle import Turtle, Screen
#time module imported to slow the snake down
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Starting Positions of the beginning turtles
POSITIONS = [(0, 0 ), (-20, 0), (-40, 0)]

#Left wall boundry on the x axis
LEFT_WALL = -380

#Right wall boundry on the x axis
RIGHT_WALL = 380

#Top wall boundry on the y axis
TOP_WALL = 380

#Bottom wall boundry on the y axis 
BOTTOM_WALL = -380

#Here a screen object is created along with its width/height - Background color set to black
#Tracer is turned off to turn animation off
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Paul's Snake Game")
screen.tracer(0)

#snake, food and score objects are created
snake = Snake()
food = Food()
score = ScoreBoard()


#Listen and onkey are called to start listening for specific key strokes 
screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")
screen.onkey(snake.up,"Up")

#While loop to keep game running
game_on = True

while game_on:
    #sleep slows/speeds the snake movement
    time.sleep(0.1)
    #update is called once the animations take place
    screen.update()
    #move is called constantly to keep the snake moving
    snake.move()

    #if the snake head is within 15 pixles of the food, a new food object is randomly generated, along with 1 point to be added to your score and the snake grows
    if snake.head.distance(food) < 15:
        food.refresh_food()
        score.add_one()
        snake.extend_snake()
        
    #If the snake head goes past the wall boundries set the game_over method is called and while loop stops
    if snake.head.xcor() < LEFT_WALL or snake.head.xcor() > RIGHT_WALL or snake.head.ycor() > TOP_WALL or snake.head.ycor() < BOTTOM_WALL:
        score.game_over()
        game_on = False

    #A for loop is run constanly comparing the snake head distance to the rest of the body, if its within 10 pixels a collision is detected and the game ends
    for position in snake.turtle_cage[1:]:
        if snake.head.distance(position) < 10:
            game_on = False
            score.game_over()

    
    
    





#keeps the screen on till you click exit
screen.exitonclick()