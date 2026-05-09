import os
import random

#clear the console
os.system("cls")

#some variables
player_health = 100
boss_health = 100
fight_status = 0
input1 = 0
damage = 0
weapon = 0

#geting the player's name and age
name = input("What is your name? ")
age = int(input("What is your age? "))

if age < 10:
    print("Sorry, you are too young to play this game.")
    exit()
else:
    while input1 < 1 or input1 > 4:
      #welcome the player
        print(f"Welcome {name}, let's start the game!")
        print("there are 4 doors in front of you.")
        print("one red door, one blue door, one green and one black .")
        input1 = int(input("Which door do you want to open? (1, 2, 3 or 4) "))
        if input1 == 1:
            print("You opened the red door and found a sna!")
            player_health = player_health - int(40)
            print(f"Your health is now {player_health}.")
        elif input1 == 2:
            print("You opened the blue door and found that it was safe!")
            player_health = player_health +int(0)
            print(f"Your health is now {player_health}.")
        elif input1 == 3:
            print("You opened the green door and found a treasure chest!")
            player_health =player_health + int(20)
            print(f"Your health is now {player_health}.")
        elif input1 == 4:
            print("You opened the black door and found it was a trap ")
            player_health = player_health - int(70)
            print(f"Your health is now {player_health}.")
        else:
            print("Invalid input, please choose a door between 1 and 4.")
        #clear console
        os.system("cls")
    
        #weapon choise
        while weapon > 4 or weapon <1:
             #weapon choise
             print("You are provided three weapon choices 1.A Sword 2.A Bow 3.Magic")
             weapon = int(input("which weapon are you chosing (1,2 or 3)"))
             if weapon == 1:
                 print("you chose a sword")
                 print("sword inflicts strong close damage")
                 damage = 30
             elif weapon == 2:
                 print("you chose a bow")
                 print("bow inflicts medium ranged damage")
                 damage = 20
             elif weapon == 3:
                 print("you chose magic")
                 print("magic inflics random damge")
             else :
                 print("invalid input retry")
            
        #boss batle bigins
        print("A boss just apeared")
        while boss_health >1 and player_health >1:
            while fight_status not in [1, 2]:  
             print("you have two options 1.run 2.fight")
             fight_status =  int(input("which one do you chose (1/2) "))
             if weapon == 3:
                 damage = random.randint(10,50)
             if fight_status == 2:
                 boss_damage = random.randint(10,30)
                 boss_health = boss_health - damage
                 if boss_health<1:
                     print("boss died you win")
                     exit()
                 print(f"{boss_health}")
                 player_health = player_health - boss_damage
                 if  player_health<1:
                     print("you lost")
                     exit()
                 print(f"{player_health}")