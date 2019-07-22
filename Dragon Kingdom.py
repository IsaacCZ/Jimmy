import random
import time

def introduction():
    print("This is the dragon kingdom!. front of you are 2 caves")
    print("one of them has a friendly dragon it will give you a treasure")
    print("The otherone is going to eat you")

def choosecave():
          cave = ""
          while cave != "1" and cave != "2":
              print("which cave you choose 1 or 2 ?")
              cave = str(input())
          return cave

def exploreCave(choosecave):
          goodCave = random.randint(1,2)
          print("You are cloeser")
          time.sleep(2)
          print("It's dark and wet")
          time.sleep(2)
          print("You are in")
          time.sleep(1)

          if goodCave == choosecave:
              print("This is your treasure")
          else:
              print("This is your end, The Dragon eat you")
        
#game
nuevojuego = "Y"

while nuevojuego == "Y":
          introduction()
          cavenumber = choosecave()
          exploreCave(cavenumber)
          print ("Quieres juegar de nuevo Y/N")
          nuevojuego = str(input()).upper()
          
          
          
          
          
          
          
