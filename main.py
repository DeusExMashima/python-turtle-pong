import turtle
from paddle import Paddle
from ball import Ball

wn = turtle.Screen() 
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600) #window size
wn.tracer(0)

paddle_a = Paddle("white", -350,0)
paddle_b = Paddle("gray", 350, 0)

ball = Ball()

#Controller

wn.listen()
wn.onkeypress(paddle_a.up, "w")
wn.onkeypress(paddle_a.down, "s")
wn.onkeypress(paddle_b.up, "Up")
wn.onkeypress(paddle_b.down, "Down")

#Main game loop
while True:
    wn.update()
    ball.move()

    #collision
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1