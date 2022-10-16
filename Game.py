import turtle
def newWindow(title,bgcolor,width,length):
    window = turtle.Screen()
    window.title(f"{title}")
    window.bgcolor(f"{bgcolor}")
    window.setup(width, length)
    window.tracer(0)
    return window
def newPlayer(shape,color,x,y):
    player= turtle.Turtle()
    player.speed(0)
    player.shape(f"{shape}")
    player.color(f"{color}")
    player.shapesize(stretch_len=1, stretch_wid=5)
    player.penup()
    player.goto(x, y)
    return player
def newball(shape,color,x,y):
    ball= turtle.Turtle()
    ball.speed(0)
    ball.shape(f"{shape}")
    ball.color(f"{color}")
    ball.penup()
    ball.goto(x, y)
    ball.dx=0.2
    ball.dy=-0.2
    return ball
def playerUp(player):
    player.sety(player.ycor()+20)
def playerDown(player):
    player.sety(player.ycor()-20)
def moveBall(ball,player1,player2,score):
   ball.setx(ball.xcor() + ball.dx)
   ball.sety(ball.ycor() + ball.dy)
   if ball.ycor()>290 or ball.ycor()<(-290):
       ball.dy*=-1
   if ball.xcor() > 390:
     score.s2+=1
     score.clear()
     score.write(f"player1: {score.s1}  player2: {score.s2}", align="center", font=24)
     ball.goto(0,0)
     ball.dx*=-1
   if ball.xcor() < -390:
      score.s1 += 1
      score.clear()
      score.write(f"player1: {score.s1}  player2: {score.s2}", align="center", font=24)
      ball.goto(0, 0)
      ball.dx *= -1
   if (ball.xcor()< -340 and ball.xcor()> -350)and (ball.ycor() < player1.ycor()+40 and ball.ycor() > player1.ycor()-40):
      ball.setx(-340)
      ball.dx *= -1
   if (ball.xcor() > 340 and ball.xcor() < 350) and ( ball.ycor() <= player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
      ball.setx(340)
      ball.dx *= -1
def Score(x):
 score=turtle.Turtle()
 score.s1=x
 score.s2=x
 score.speed(0)
 score.color("white")
 score.penup()
 score.hideturtle()
 score.goto(0,250)
 score.write(f"player1: {score.s1}  player2: {score.s2}",align="center",font=24)
 return score