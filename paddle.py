import turtle

# paddle_a = turtle.Turtle()
# paddle_a.speed(0) #speed for animation
# paddle_a.shape("square")
# paddle_a.color("white")
# paddle_a.penup()
# paddle_a.goto(-350, 0)

class Paddle(turtle.Turtle):
    def __init__(self, color, goto_a, goto_b):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color(color)
        self.penup()
        self.goto(goto_a, goto_b)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.y = self.ycor()

    def up(self):
        if self.ycor() < 350:
            self.y += 20
            self.sety(self.y)

    def down(self):
        if self.ycor() > -350:
            self.y -= 20
            self.sety(self.y)