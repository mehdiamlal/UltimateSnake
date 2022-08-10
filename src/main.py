from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Ultimate Snake")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    snake.move()

    #food collision handling
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.grow()
        food.refresh()
    
    #wall collision handling
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    #tail collision handling
    for s in snake.segments[1:]:      #this way we are not considering the head
        if snake.head.distance(s) <= 5:
            scoreboard.game_over()
            game_is_on = False

    screen.update()
    time.sleep(0.1)



screen.exitonclick()