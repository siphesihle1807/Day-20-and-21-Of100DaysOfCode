from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# Displays screen and specifications
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Siphe's Snake Game.")
screen.tracer(0)

# displays created snake in the snake module
# snake controls
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

#   Detects the movement of the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_increase()

# Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.end_game()

# Detect collision with tail
# if head collides with any segments in body, trigger end_game
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.end_game()




screen.exitonclick()