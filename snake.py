from turtle import Turtle
STARTING_POSITIONS = [(0,0) , (-20,0), (-40,0)]
Move_Distance = 20
UP = 90
DOWN = 270 
RIGHT = 0 
LEFT = 180

class Snake:

    def __init__(self):
        self.collect_segments = []
        self.create_snake()
        self.head = self.collect_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS: 
            segment = Turtle('square') 
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.collect_segments.append(segment)
    
    def move(self):               
            for seg_num in range(len(self.collect_segments)-1, 0,-1):

                new_x = self.collect_segments[seg_num - 1].xcor()
                new_y = self.collect_segments[seg_num - 1].ycor()

                self.collect_segments[seg_num].goto(new_x,new_y)
            self.head.forward(20)
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
