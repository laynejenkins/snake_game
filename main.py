from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# create starting Snake, Food pellet, and Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# create user control inputs to move snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# game logic
while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food and generate new food if "eaten"
    if snake.head.distance(food) < 15:
        food.refresh()


screen.exitonclick()
