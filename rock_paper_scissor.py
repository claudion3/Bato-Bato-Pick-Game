#import getpass to hide player choice
import getpass


#Discription of the game
print('This game call Rock, Paper, Scissors\n(aka \"Ro-Sham-Bo\", janken, \"Bato, Bato, Pick\"  and \"Scissors, Paper, Stone\")')
print('It\'s easy to play it, just follow the instruction\n')

#name of the players
A_player=input("Player number 1, Please enter your name: ")
print(A_player)
B_player=input("Player number 2, Please enter your name: ")
print(B_player,"\n")
#choice of the players
print("1)Rock\n2)Paper\n3)Scissor\n")
 
#entering the choice
A_choose=int(getpass.getpass("Enter the number of your choose: "))
B_choose=int(getpass.getpass("Enter the number of your choose: "))
    
#function of game
def game(a,b):
    if(a==1 and b==2):
        print("The winner is ",B_player)
    elif(a==1 and b==3):
        print("The winner is ",A_player)
    elif(a==1 and b==1):
        print("Try again")
    elif(a==2 and b==1):
        print("The winner is ",A_player)
    elif(a==2 and b==3):
        print("The winner is ",B_player)
    elif(a==2 and b==2):
        print("Try again")
    elif(a==3 and b==1):
        print("The winner is ",B_player)
    elif(a==3 and b==1):
        print("The winner is ",B_player)
    elif(a==3 and b==2):
        print("The winner is ",A_player)
    elif(a==3 and b==3):
        print("Try again")
    else:
        print("Invalid input")

#call the function
game(A_choose,B_choose)