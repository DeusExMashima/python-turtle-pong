import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.goto(0, 0)
        self.dx = 2
        self.dy = 2
    
    #move the ball
    def move(self):
        
        self.setx(self.xcor()+self.dx)
        self.sety(self.ycor()+self.dy)

        if self.ycor() > 290:
            self.sety(290)
            self.change_dy()
        elif self.ycor() < -290:
            self.sety(-290)
            self.change_dy()

        if self.xcor() > 390:
            self.goto(0, 0)
            self.change_dx()
        elif self.xcor() < -390:
            self.goto(0,0)
            self.change_dx()
    
    def change_dx(self):
        self.dx *= -1

    def change_dy(self):
        self.dy *= -1