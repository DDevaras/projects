print("Hello user!, you have entered the dice game.") 
hello = input("Welcome to the game, (Press Enter to continue)")
choice = input("You get to choose which dice you would like to roll, Press Enter to continue ")

#A GUI appears on the screen which allows you too choose what dice you want to use

import random
import time

from tkinter import *
app = Tk()
app.title("Dice Game")
app.geometry('400x100+200+100')

lab = Label(app, text='Choose which dice you would like to use! ', height = 3)
lab.pack()



def b1_click():
    print("\nYou have selected to use the 2 sided dice!")
    print("\nLet's start, roll the dice")

def b2_click():
    print("\nYou have selected to use the 4 sided dice!")
    print("\nLet's start, roll the dice")

def b3_click():
    print("\nYou have selected touse the 8 sided dice!")
    print("\nLet's start, roll the dice")

def b4_click():
    print("\nYou have selected to use the 6 sided dice!")
    print("\nLet's start, roll the dice")


b1 = Button(app, text = "2 Sided dice", width = 10, command = b1_click)
b1.pack(side = 'left', padx = 10, pady = 10)
b2 = Button(app, text = "4 sided dice", width = 10, command = b2_click)
b2.pack(side = 'left', padx = 10, pady = 10)
b3 = Button(app, text = "8 sided dice", width = 10, command = b3_click)
b3.pack(side = 'right', padx = 10, pady = 10)
b4 = Button(app, text = "6 sided dice", width = 10, command = b4_click)
b4.pack(side = 'right', padx = 10, pady = 10)
app.mainloop()



def main():
    player1 = 0
    player1wins = 0
    player2 = 0
    player2wins = 0
    rounds = 1
 
    while rounds != 4:
        print("\nRound " + str(rounds))
        player1 = dice_roll()
        time.sleep(4)
        player2 = dice_roll()
        print("Player 1 Roll: " + str(player1))
        time.sleep(4)
        print("Player 2 Roll: " + str(player2))
 
        if player1 == player2:
            time.sleep(4)
            print("Draw!\n")
        elif player1 > player2:
            player1wins = player1wins + 1
            time.sleep(4)
            print("Player 1 wins!\n")
        else:
            player2wins = player2wins + 1
            time.sleep(4)
            print("Player 2 wins!\n")
 
        rounds = rounds + 1
   
    if player1wins == player2wins:
        time.sleep(4)
        print("It's a Draw!")
    elif player1wins > player2wins:
        time.sleep(4)
        print("You win! - Rounds Won: " + str(player1wins))
        time.sleep(4)
    else:
        print("I win!  - Rounds Won: " + str(player2wins))

 
def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll

main()

screen = input("\nPlay again or press q to quit")

if input == 'q':
    print("\nGame over, it was fun playing!")
    time.sleep(4)
else:
    print("Let's play again!")
    
