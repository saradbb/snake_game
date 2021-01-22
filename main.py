from turtle import Screen
import time
from Snake import Snake
from food import Food
from Scoreboard import Score
screen = Screen()

#A SNAKE GAME I USED TO PLAY IN NOKIA PHONES WHEN I WAS A KID


def initialize_screen():
    """
    Initialize the screen
    :return:
    """
    global screen
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.bgcolor("black")
    screen.title("Snake Game")

def check_border():
    """
    Check if the snake has touched the 'INVISIBLE' edge
    :return: false is the edge is touched, true otherwise
    """
    global snake
    if snake.head.xcor() > 260 or snake.head.xcor() < -260 or snake.head.ycor() > 260 or snake.head.ycor() < -260:
        return False
    return True



def check_collision():
    """
    Check if snake has touched its own body
    :return: false is touched, true otherwise
    """
    for part in snake.snakebody:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 10:
            return False
    return True



def game():
    """
    This is the function where the game is played
    :return:
    """
    global screen,food,score
    game_on = True
    while game_on:    #Unless the edge is touched or the screen touches itsself
        screen.update()   #Every change is accumulated and updated once
        time.sleep(.1)
        snake.move()
        if snake.head.distance(food) < 15:    #It means snake has eaten the food
            score.update()      #update score
            food.new_position()   #Generate new food
            snake.extend()      #Make snake longer
        game_on = check_border()    #Check if the snake touched the border
        if game_on:    #If it hasnot check if it has touched its body
            game_on = check_collision()
    score.game_over()


snake = Snake()
screen.listen()
screen.onkey(key="Up", fun = snake.up)
screen.onkey(key="Down", fun = snake.down)
screen.onkey(key="Left", fun = snake.left)
screen.onkey(key="Right", fun = snake.right)


food = Food()
score = Score()
initialize_screen()
game()

screen.exitonclick()
