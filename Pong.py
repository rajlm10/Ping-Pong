import turtle
import os 
#Setting up screen
so=turtle.Screen()
so.bgcolor("black")
so.title("Pong")
so.setup(width=800,height=600)
so.tracer(0) #Lets up speed up game

#Paddle A
paddleA=turtle.Turtle()
paddleA.speed(0) #speed of animation is max
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5,stretch_len=1)
paddleA.penup() #so it doesnt draw
paddleA.goto(-350,0)

#Paddle B
paddleB=turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5,stretch_len=1)
paddleB.penup() 
paddleB.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0) 
ball.shape("circle")
ball.color("white")
ball.penup() 
ball.goto(0,0)
#Ball movement
ball.dx=2 #delta change in pixels by 2
ball.dy=-2


#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0",align="center",font=("Courier",24,"italic"))

#Score
scoreA=0
scoreB=0

#Moving the paddles
def paddleAup():
    y=paddleA.ycor()
    y+=20
    paddleA.sety(y)

def paddleAdown():
    y=paddleA.ycor()
    y-=20
    paddleA.sety(y)

def paddleBup():
    y=paddleB.ycor()
    y+=20
    paddleB.sety(y)

def paddleBdown():
    y=paddleB.ycor()
    y-=20
    paddleB.sety(y)

#Binding to Keyboard
so.listen()
so.onkeypress(paddleAup,"w")
so.onkeypress(paddleAdown,"s")
so.onkeypress(paddleBup,"Up")
so.onkeypress(paddleBdown,"Down")




#Main game loop
while True:
    so.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #Border Checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1 #Reverses direction
        os.system("afplay bounce.wav&") #& does not pause game while sound plays

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        os.system("afplay bounce.wav&")

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        scoreA+=10
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA,scoreB),align="center",font=("Courier",24,"italic"))
        
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        scoreB+=10
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA,scoreB),align="center",font=("Courier",24,"italic"))


    #Paddle-ball collision
    if (ball.xcor()>340 and ball.xcor()<350 ) and (ball.ycor()<paddleB.ycor()+40 and ball.ycor()>paddleB.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
        os.system("afplay bounce.wav&")

    if (ball.xcor()<-340 and ball.xcor()>-350 ) and (ball.ycor()<paddleA.ycor()+40 and ball.ycor()>paddleA.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1
        os.system("afplay bounce.wav&")

#so.mainloop()
