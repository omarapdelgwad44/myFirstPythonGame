import Game
Window1=Game.newWindow("pingPong","black",800,600)
player1=Game.newPlayer("square","red",-350,0)
player2=Game.newPlayer("square","blue",350,0)
ball=Game.newball("circle","white",0,0)
score = Game.Score(0)
Window1.listen()
Window1.onkeypress(lambda player=player1:Game.playerUp(player),"w")
Window1.onkeypress(lambda player=player1:Game.playerDown(player),"s")
Window1.onkeypress(lambda player=player2:Game.playerUp(player),"Up")
Window1.onkeypress(lambda player=player2:Game.playerDown(player),"Down")
while True:
  try:
    Window1.update()
    Game.moveBall(ball,player1, player2,score)
  except:
    break

