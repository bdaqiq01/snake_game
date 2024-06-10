from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
score = 0
screen.title('Snake Game')

screen.tracer(0)
mySnake = Snake()
myFood = Food()

myScoreBoard = ScoreBoard()
myScoreBoard.show_score()

screen.listen()  #since it is listening it keeps listening
screen.onkey(mySnake.up, "Up")
screen.onkey(mySnake.down, "Down")
screen.onkey(mySnake.left, "Left")
screen.onkey(mySnake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    mySnake.move()
    #collision detect
    if myFood.distance(mySnake.head) < 15:
        myScoreBoard.add_score()
        mySnake.add_seg()
        myScoreBoard.clear()
        myScoreBoard.show_score()
        myFood.food_move()
    if abs(mySnake.head.xcor()) > 295 or abs(mySnake.head.ycor()) > 295:
        myScoreBoard.game_over()
        game_is_on = False
    #detect collison with itself
    for seg in mySnake.segments[2:]:
        if seg.distance(mySnake.head) < 10:
            myScoreBoard.game_over()
            game_is_on = False




screen.exitonclick()
