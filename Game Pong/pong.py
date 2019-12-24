# Part 1: Getting Started
# Module that work good with simple games, normaly people use pygame
import turtle

wm = turtle.Screen()
wm.title("Pong with Python")
wm.bgcolor("black")
wm.setup(width=800, height=600)
# that stops the window to automatic update and serves to speed up the game
wm.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2


# Function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)
	
def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)
	

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)
	
def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)
	
# keyboard binding
wm.listen()
wm.onkeypress(paddle_a_up, "w")
wm.onkeypress(paddle_a_down, "s")
wm.onkeypress(paddle_b_up, "Up")
wm.onkeypress(paddle_b_down, "Down")
	

# Main game loop
while True:
	wm.update()
		
