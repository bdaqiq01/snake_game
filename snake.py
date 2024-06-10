from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.length = 3
        self.segments = []
        for i in range(self.length):
            seg_body = Turtle(shape="square")
            seg_body.penup()
            seg_body.color("white")
            seg_body.goto(x=i * (-20), y=0)
            self.segments.append(seg_body)
        self.head = self.segments[0]

    def add_seg(self):
        new_seg = Turtle(shape="square")
        new_seg.penup()
        new_seg.color("white")
        self.segments.append(new_seg)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def up(self): #have to move the first one 90
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self): #have to move the first one 90
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self): #have to move the first one 90
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self): #have to move the first one 90
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




