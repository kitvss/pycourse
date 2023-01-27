print("...rock...\n...paper...\n...scissors...")
player1 = input("Enter Player 1's choice:\n")
player2 = input("Enter Player 2's choice:\n")
# winning = "paper"
# winner = None
# if player1 == winning:
# 	winner = player1
# elif player2 == winning:
# 	winner = player2
# print("Shoot!")
# if (player1 != "paper" or player1 != "rock" or player1 != "scissors") and (player2 != "paper" or player2 != "rock" or player2 != "scissors"):
# 	print("please input valid value")
# elif player1 == winning or player2 == winning:
# 	print(f"{winner} is a winner")

# if player1 == player2:
# 	print("try again, no winner")
# elif winning == player2:
# 	print("player2 is a winner")
# elif winning == player1:
# 	print("player1 is a winner")
# else:
# 	print("something is wrong, try again")

# rock hits scissors
# scissors cut paper
# paper covers rock

if player1 == "rock" and player2 == "scissors":
	print("player1 win")
elif player1 == "rock" and player2 == "paper":
	print("player2 win")
elif player1 == "paper" and player2 == "scissors":
	print("player2 win")
elif player1 == "paper" and player2 == "rock":
	print("player1 win")
elif player1 == "scissors" and player2 == "paper":
	print("player1 win")
elif player1 == "scissors" and player2 == "rock":
	print("player2 win")
elif player2 == player1:
	print("it's a tie")
else:
	print("something went wrong")