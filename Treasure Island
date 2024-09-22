print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''') # use triple quote to print multi line.

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

question_1=input('You\'re at a cross road.    Where do you want to go?\nleft or right').lower()   #.lower because user can give capital also
if question_1=='left':
    question_2 = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. \nType "swim" to swim across.\n').lower()
    if question_2 == 'wait':
        question_3=input('You arrive at the island unharmed.\n There is a house with 3 doors.\nOne red, one yellow and one blue.\n Which colour do you choose?\n').lower()
        if question_3 == 'red':
            print("GAME OVER\nBurnt by fire")
        elif question_3 =='blue':
            print('GAME OVER\nEaten by beast')
        elif question_3=='yellow':
            print('You found the treasure! You Win!')
        else:
            print('GAME OVER')
    else:
        print('Attack by trout\nGAME OVER')

else:
    print('Fall into a hole\nGAME OVER')

