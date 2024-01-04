'''
1. Plan out what you need to do 
2. Annotate your code (put comments describing section)
3. Good variable naming
'''
'''
1. Create player turtle
2. Be able to move turtle
3. Be able to shoot
4. Make one row of enemies not moving
5. Make them move together
6. Make complex moving
7. Duplicate rows of enemies
8. Kill code
'''
'''
1. Get 100 points for every alien you Kill
2. Change the background 
3. Make a reset button that moves the aliens back into position
a. Put sections of code into functions: inititateGame(), runGame()

'''
outList = []
insideList1 = [1, 2, 3, 4]
insideList2 = [5, 6, 7, 8]
insideList3 = [9, 10, 11, 12]
outList = [insideList1, insideList2, insideList3]
print(outList)

for li in outList:
  print(li)
  for lit in li:
    print(lit)
    


#import code
import turtle
import time 

player = turtle.Turtle()

#player position
player.penup()
player.goto(0,-175)
player.left(90)

#player moving
playerx = 0
def playerleft():
  global playerx
  playerx = playerx - 5
  player.goto(playerx,-175)
  screen.update()
  
def playerright():
  global playerx
  playerx = playerx + 5
  player.goto(playerx,-175)
  screen.update()
  
#player keys
screen = turtle.Screen()
screen.onkey (playerleft,"left")
screen.onkey (playerright, "right")
screen.listen()
screen.tracer(0)

#player shoot
lastTime = time.time()

def shoot():
  global lastTime
  if lastTime + 1 < time.time():
    bullet = turtle.Turtle()
    bullet.penup()
    bullet.color("red")
    bullet.goto(player.xcor(),player.ycor())
    bullet.right(-90)
    lastTime = time.time()
    for i in range(789):
      bullet.forward(2)
      screen.update()
      for alien_row in all_aliens:
        for alien in alien_row:
          if abs(alien.xcor()-bullet.xcor()) < 10 and abs(alien.ycor()-bullet.ycor()) < 10:
            alien.goto (0,3000)

#bullet keys
screen.onkey (shoot, "space")

#aliens
all_aliens = []
alien_row = []

x = -225
y = 500
for i in range (3):
  for i in range(10):
    alien = turtle.Turtle()
    alien.penup()
    alien.shape("turtle")
    alien.right(90)
    alien.goto(x,y)
    screen.update()
    alien_row.append(alien)
    x = x + 50
  all_aliens.append(alien_row)
  alien_row = []
  y = y - 50
  x = -225


def moveAllAliens(all_aliens):
  amt =1
  for alienrow in all_aliens:
    for alien in alienrow:
      alien.goto(alien.xcor()+3,alien.ycor())
      time.sleep(amt)
      alien.goto(alien.xcor()+3,alien.ycor())
      time.sleep(amt)
      alien.goto(alien.xcor(),alien.ycor()-3)
      time.sleep(amt)
      if alien.ycor() < -175:
        Death = True
      alien.goto(alien.xcor()-3,alien.ycor())
      time.sleep(amt)
      alien.goto(alien.xcor()-3,alien.ycor())
      time.sleep(amt)
      alien.goto(alien.xcor(),alien.ycor()-3)
      time.sleep(amt)
      if alien.ycor() < -175:
        Death = True
'''
      move all aliens left x times
      move all aliens down y times
        check all coordinates
'''

#Die/Speed of aliens
speed = 1
Death = False
while True:
  for alienrow in all_aliens:
    for alien in alienrow:
      moveAllAliens(all_aliens)
      screen.update()
  if Death == True:
    player.write("Gameover",font=("Arial", 50, "normal"))
    break
      
        
  speed = speed + 0.25
