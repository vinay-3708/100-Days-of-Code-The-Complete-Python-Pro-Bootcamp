from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for _ in STARTING_POSITION:
            snake = Turtle()
            snake.penup()
            snake.shape("square")
            snake.color("white")
            snake.goto(x= _[0], y=_[1])
            self.snake_body.append(snake)
    
    def move(self):
        for self.body in range(len(self.snake_body)-1,0,-1):
            x = self.snake_body[self.body -1].xcor()
            y = self.snake_body[self.body -1].ycor()
            self.snake_body[self.body].goto(x,y)
        self.snake_body[0].forward(20)

    def snake_position(self):
        return self.snake_body[0].heading()

    def up(self):
        self.pos = self.snake_position()
        if self.pos == 0:
            self.snake_body[0].left(90)
        if self.pos == 180:
            self.snake_body[0].right(90)
         

    def down(self):
        self.pos = self.snake_position()
        if self.pos == 0:
            self.snake_body[0].right(90)
        if self.pos == 180:
            self.snake_body[0].left(90)

    def left(self):
        self.pos = self.snake_position()
        if self.pos == 90:
            self.snake_body[0].left(90)
        if self.pos == 270:
            self.snake_body[0].right(90)

    def right(self):
        self.pos = self.snake_position()
        if self.pos == 90:
            self.snake_body[0].right(90)
        if self.pos == 270:
            self.snake_body[0].left(90)