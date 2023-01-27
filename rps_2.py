print("...rock...\n...paper...\n...scissors...")
player1 = input("Enter Player 1's choice:\n")
print("No cheating!\n\n" * 20)
player2 = input("Enter Player 2's choice:\n")


if player1 == player2:
    print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("player1 win")
    elif player2 == "paper":
        print("player2 win")
elif player1 == "paper":
    if player2 == "rock":
        print("player1 win")
    elif player2 == "scissors":
        print("player2 win")
elif player1 == "scissors":
    if player2 == "paper":
        print("player1 win")
    elif player2 == "rock":
        print("player2 win")
else:
    print("something went wrong")



# if player1 == "rock" and player2 == "scissors":
# 	print("player1 win")
# elif player1 == "rock" and player2 == "paper":
# 	print("player2 win")
# elif player1 == "paper" and player2 == "scissors":
# 	print("player2 win")
# elif player1 == "paper" and player2 == "rock":
# 	print("player1 win")
# elif player1 == "scissors" and player2 == "paper":
# 	print("player1 win")
# elif player1 == "scissors" and player2 == "rock":
# 	print("player2 win")
# elif player2 == player1:
# 	print("it's a tie")
# else:
# 	print("something went wrong")