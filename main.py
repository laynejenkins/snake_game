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
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food and generate new food if "eaten". Also, increase score by 1 and add 1 new segment to snake tail.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall. Triggers game over.
    if not -300 < snake.head.xcor() < 300 or not -300 < snake.head.ycor() < 300:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail. Triggers game over.
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
