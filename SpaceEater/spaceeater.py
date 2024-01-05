#Annotation your code 

#This section creates all the balls

#this loops through all the balls
#smart variable naming
#Write pseudocdoe to outline

'''
Import code
Make score turtle
Draw box
moving turtle
balls
'''
#import code
import turtle 
import random
score = turtle.Turtle()
box = turtle.Turtle()
r = turtle.Turtle()

#score code
score.penup()
score.goto(-200,200)
x = 1
#while True:
  #score.write(x)
  #score.clear()
  #x = x+1
  
#box code
box.speed(0)
box.penup()
box.goto (-200,200)
box.pendown()
box.color("red")
for i in range(4):
  box.forward(400)
  box.right(90)


 
#player
def right():
  r.right(10)
def left():
  r.left(10)
  
screen = turtle.Screen()
screen.listen()
screen.onkey(right,"right")
screen.onkey(left,"left")
screen.tracer(0)

#balls code
balls = []
for i in range(10):
  screen.update()
  ball = turtle.Turtle()
  balls.append(ball)
#Create all the balls and set direction of balls
for ball in balls:
  ball.speed(0)
  ball.color("red")
  ball.penup()
  ball.shape("circle")
  ball.goto(random.randint(-200,200),random.randint(-200,200))
  ball.right(random.randint(0,360))

def insidebounds(turt):
  #Statement that checks 4 boundaries of box
  return turt.xcor()>200 or turt.xcor()<-200 or turt.ycor()>200 or turt.ycor()<-200
while True:
  r.forward(5)
  screen.update()
  if insidebounds(r):
    r.right(180)
  
  for ball in balls:
    ball.forward(5)
    if insidebounds(ball):
      ball.right(180)
    if abs(ball.xcor() - r.xcor()) < 10 and abs(ball.ycor() - r.ycor()) < 10:
      ball.ht()
      score.clear()
      score.write(x)
      x = x+1





