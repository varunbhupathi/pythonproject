# main.py
import random
'''
Write out every function you will create 
1. purpose
2. inpout
3. output 

1 Start
  a Greeting
  b start game
  
2 dealer
  a Max 15
  Create hand
  If hand < 15:
    Add random card
  else:
    return hand

3 player_hand:
  crete hand
  Give player 2 cards
    f
  ask player stay or hit
  If hit:
   give reandom card
  else:
  tell dealer hand and make winner
'''

def main():
  print("It is blackjack! The values of the cards are 2-11.")
  print("Got it!")
  startGTame()
  
def startGTame():
  hand = [random.randint(2,11), random.randint(2,11)]
  print(f"Your hand is {hand}")
  checkvalue(hand)
  while True:
    choice = input("Do you want to hit or stay? ")
    if choice == "hit":
      getCard(hand)
      checkvalue(hand)
    if choice == "stay":
      Compare(hand) 
      hand = []
    
def getCard(hand):
  print(f"Your hand is {hand}.")
  hand.append(random.randint(2,11))
  print(f"Your new hand is {hand}.")

def Dealer_hand():
  Dhand = []
  while True:
    TDhand = 0
    for i in range(len(Dhand)):
      TDhand += Dhand[i]
    if TDhand < 15:
      Dhand.append(random.randint(2,11))
    else:
      return TDhand

def checkvalue(hand):
  Thand = 0
  for i in range(len(hand)):
    Thand += hand[i]
  if Thand > 21:
    print("Bust!!!!!")
    startGTame()
  if Thand == 21:
    print("You win!!")
    startGTame()

def Compare(hand):
  Thand = 0
  Dhand = Dealer_hand()
  for i in range(len(hand)):
    Thand += hand[i]
  if Dhand > 21:
    print("Player has won!")
    print(f"Dealer total hand was {Dhand}. (Bust)")
    startGTame()
  elif Thand > Dhand:
    print("Player has won!")
    print(f"Dealer total hand was {Dhand}.")
    startGTame()
  elif Dhand > Thand:
    print("Dealer won!")
    print(f"His total hand was {Dhand}.")
    startGTame()
  else:
    print(f"The game has tied at {Thand}")
    startGTame()
main()
