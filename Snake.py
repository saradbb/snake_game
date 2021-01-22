from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.INITIAL_X = 0
        self.INITIAL_Y = 0
        self.current_x = self.INITIAL_X
        self.current_y = self.INITIAL_Y
        self.snakebody = []
        self.initialize_snake()
        self.head = self.snakebody[0]
        self.head.setheading(RIGHT)  #INITIALLy points to 0degree

    def initialize_snake(self):
        #Initially has 3 blocks to the body
        for i in range(0, 3):
            temp_snake = Turtle()
            temp_snake.color("white")
            temp_snake.shape('square')
            temp_snake.penup()
            temp_snake.setx(self.current_x)
            temp_snake.sety(self.current_y)
            self.current_x -= 20
            self.snakebody.append(temp_snake)


    def move(self):
        """
        This function takes individual block, starting from the last one, moves it to its predecessor's position and
        moves the head based on user's input
        :return:
        """
        for i in range(len(self.snakebody) - 1, 0, -1):
            new_x = (self.snakebody[i - 1].xcor())
            new_y = (self.snakebody[i - 1].ycor())
            self.snakebody[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



    def extend(self):
        """
        Add new block when the food is eaten
        :return:
        """
        current_pos = self.snakebody[-1].pos()
        new_part =Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(current_pos)
        self.snakebody.append(new_part)



