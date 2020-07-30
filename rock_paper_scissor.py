#import getpass to hide player choice
import random
from threading import Timer
import asyncio


#Discription of the game
print('This game call Rock, Paper, Scissors\n(aka \"Ro-Sham-Bo\", janken, \"Bato, Bato, Pick\"  and \"Scissors, Paper, Stone\")')
print('It\'s easy to play it, just follow the instruction\n')

 
 
def winner(a,b):
    if a=="Rock" and b=="Paper":
        print("Machine win")
    elif a=="Rock"and b=="Scissor":
        print("you win")
    elif a=="Paper"and b=="Scissor":
        print("Machine win")
    elif a=="Paper"and b=="Rock":
        print("you win")
    elif a=="Scissor"and b=="Paper":
        print("you win")
    elif a=="Scissor"and b=="Rock":
        print("Machine win")
    else:
        print("null")

   
  
async def main():
    A_player=input("Please enter your name: ")
    print("1)Rock\n2)Paper\n3)Scissor\n")
    A_choose=int(input(A_player+ " Enter the number of your choose: "))
    
    if A_choose==1:
        A_playerChoice="Rock"
    elif A_choose==2:
        A_playerChoice="Paper"   
    elif A_choose==3:
        A_playerChoice="Scissor"
    else:
        A_playerChoice="error"
    print(A_player+" choose  "+ A_playerChoice)
     

    await asyncio.sleep(2)     
    answer = ["Rock", "Paper", "Scissor"]
    B_playerChoice=random.choice(answer)
    print("Machine choose  "+B_playerChoice)
    await asyncio.sleep(3)
    winner(A_playerChoice,B_playerChoice)
    
asyncio.run(main())




 