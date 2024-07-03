from turtle import Screen, Turtle 
from snake import Snake
import time

Display = Screen()
Display.setup(width=600,height=600) 
Display.bgcolor('black')
Display.title('My Snake Game')

Display.tracer(0)

snake = Snake()

Display.listen()
Display.onkey(snake.up, 'Up')
Display.onkey(snake.down, 'Down')
Display.onkey(snake.left, 'Left')
Display.onkey(snake.right, 'Right')




game_is_on = True 

while game_is_on:
    Display.update() 
    time.sleep(0.1)
    snake.move()
    














Display.exitonclick()