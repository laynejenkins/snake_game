from turtle import Screen
from snake import Snake
import time

# setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# create starting Snake
snake = Snake()

# create user control inputs to move snake in directions
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# game logic
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
