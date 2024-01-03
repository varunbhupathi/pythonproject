import random
import time

# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()

# Write the pseudocode 
'''
Welcome stuff
Ready set go
Give them the letters
get them to enter a words
score them
Repeat the last two steps forever
'''
#What function will you create?


#What data structures will you need touse and why?

def welcome():
  Score = 0
  print("Welcome to the game that you can only use 7 letters given to make the most words.")
  time.sleep(1)
  print('Ready')
  time.sleep(1)
  print('Set')
  time.sleep(1)
  print('Type')
  start = time.time()
  while True:
    now = time.time()
    if now - start > 20:
      print("You slow")
      return
    gameletters = letters() 
    while not any(x in gameletters for x in ["a", "e", "i", "o", "u", "y"]):
      gameletters = letters()
    print(gameletters)
    if checkword(gameletters) == "Lose":
      Score -= 1
      print(f"You have this {Score} as your score.")
    else:
      Score +=1
      print(f"You have this {Score} as your score.")

  
  
def letters():
  abcletters = 'abcdefghijklmnopqrstuvwxyz'
  gameletters = []
  print()
  for i in range(7):
    num = random.randint(0,len(abcletters)-1)
    gameletters.append(abcletters[num])
    abcletters = abcletters.replace(abcletters[num], "")
  return gameletters

# What is the input and what is the output? How is the function going to be used?
# Input: gameletters(the letters used in the game)
# Output: Tells you if whatever the user put in is worth a point or nah.
def checkword(gameletters):
  word = input("What is your guess? ")
  if word not in validWords:
    print("Untitelahs[")
  for i in range(len(word)):
    if word[i] not in gameletters:
      print("Xbox lost")
      return "Lose"
  print(word)
  


welcome()


'''
abcletters = "alltheletters"
gameletters = []
for i in rangaeg adsljkheasef abcdefghijklmnopqrstuvwxyz
  num = random number fron 0 - len(abcletters)
  gameletters.append(abcletters[num])
  abcletters = abcletters.replace(abcletters[num], "")
  
'''















