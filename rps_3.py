import random

print("...rock...\n...paper...\n...scissors...")
player = input("Enter Player 1's choice:\n").lower()
#player = player.lower() #this is to make it not sensetive to the case
computer = random.randint(0, 2)

if computer == 0:
    computer = "rock"
elif computer == 1:
    computer = "paper"
elif computer == 2:
    computer = "scissors"

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("player win")
    elif computer == "paper":
        print("computer win")
elif player == "paper":
    if computer == "rock":
        print("player win")
    elif computer == "scissors":
        print("computer win")
elif player == "scissors":
    if computer == "paper":
        print("player win")
    elif computer == "rock":
        print("computer win")
else:
    print("something went wrong")

print(f"computer choosed {computer}")