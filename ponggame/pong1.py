#screen
import turtle
import winsound

window=turtle.Screen()
window.title("Pong Game by Harsha Reddy")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

#score change
score1=0
score2=0

#paddle 1
paddle1=turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("black")
paddle1.shapesize(stretch_wid=6,stretch_len=0.5)
paddle1.penup()
paddle1.goto(-350,0)


#paddle 2
paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("black")
paddle2.shapesize(stretch_wid=6,stretch_len=0.5)
paddle2.penup()
paddle2.goto(350,0)


#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx=0.4
ball.dy=0.4

#scores
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1 = 0  Player 2 = 0",align="center",font=("Courier",24,"normal"))
def paddle1up():
    y=paddle1.ycor()
    y+=20
    paddle1.sety(y)
def paddle1down():
    y=paddle1.ycor()
    y-=20
    paddle1.sety(y)

def paddle2up():
    y=paddle2.ycor()
    y+=20
    paddle2.sety(y)
def paddle2down():
    y=paddle2.ycor()
    y-=20
    paddle2.sety(y)

window.listen()
window.onkeypress(paddle1up,"w")
window.onkeypress(paddle1down,"s")

window.onkeypress(paddle2up,"Up")
window.onkeypress(paddle2down,"Down")

#screen stillness and updation
while True:
    window.update()

    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #borders
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score1+=1
        pen.clear()
        pen.write("Player 1 = {}  Player 2 = {}".format(score1,score2), align="center", font=("Courier", 24, "normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score2+=1
        pen.clear()
        pen.write("Player 1 = {}  Player 2 = {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    #paddle bounce
    if (ball.xcor()>340  and ball.xcor()<350) and  (ball.ycor()<paddle2.ycor()+ 50 and ball.ycor()>paddle2.ycor()-50):
        ball.setx(340)
        ball.dx *=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball.xcor()<-340  and ball.xcor()>-350) and  (ball.ycor()<paddle1.ycor()+ 50 and ball.ycor()>paddle1.ycor()-50):
        ball.setx(-340)
        ball.dx *=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)