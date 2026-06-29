import random

while True:
    choices=["rock","paper","scessiors"]
    computer=random.choice(choices)
    player=None

    while player not in choices:
     player=input("rock , paper , scessiors ?:").lower()

    if player==computer:
     print("computer :",computer)
     print("player :",player)
     print("Tie")

    elif player=="rock":
        if computer=="paper":
         print("computer :",computer)
         print("player :",player)
         print("You lose !")
        if computer=="scessiors":
         print("Computer :",computer)
         print("player :",player)
         print("You win")

    elif player=="paper":
        if computer=="scessiors":
         print("computer :",computer)
         print("player :",player)
         print("You lose !")
        if computer=="rock":
            print("computer :",computer)
            print("player :",player)
            print("you win !")

    elif player=="scessiors":
        if computer=="rock":
               print("computer :",computer)
               print("player :",player)
               print("You lose !")
        if computer=="paper":
                 print("computer :",computer)
                 print("player :",player)
                 print("You win !")
    play_again=input("play_again (yes/no) ?").lower()
    if play_again != "yes":
        break
print("Bye")