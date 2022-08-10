from turtle import Turtle
STARTING_POSITINS = [(20, 0), (0, 0), (-20, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

def format_component(c, pos):
    """Formats the c turtle and gives it an initial position of pos."""
    c.penup()
    c.shape("square")
    c.color("#fff")
    c.setpos(pos)

class Snake:


    def __init__(self):
        self.segments = [Turtle(), Turtle(), Turtle()]    #representation of the snake

        for i in range(len(self.segments)):
            format_component(self.segments[i], STARTING_POSITINS[i])
        
        self.head = self.segments[0]


    def move(self):
        """Makes the snake move forward by 20."""
        for s in self.segments:
            if s == self.head:
                next_position = s.pos()
                s.forward(20)
            else:
                actual_position = s.pos()
                s.goto(next_position)
                next_position = actual_position


    def up(self):
        """Makes the snake head turn up."""
        if self.head.heading() != DOWN:     #this way it doesn't turn on itself, same logic for the following three methods
            self.head.setheading(UP)


    def down(self):
        """Makes the snake head turn down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        """Makes the snake head turn left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        """Makes the snake head turn right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        """Grows the snake by one block"""
        self.segments.append(Turtle())
        format_component(self.segments[-1], self.segments[-2].pos())