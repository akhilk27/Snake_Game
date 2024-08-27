from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)       # To turn off updates of the turtle

snake = Snake()
food = Food()
score = Score()

# To listen to the key strokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Moves the Snake
game_on = True
while game_on:
    screen.update()         # To update the position of the turtle each time all the segments move
    time.sleep(0.1)

    snake.move()

    # Detects collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        score.increase_score()

    # Detects collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        print("Game Over")
        game_on = False
        score.game_over()

    # Detect collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

    # If the Head collides with any segment of the body, the game will be terminated

screen.exitonclick()

