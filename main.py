CHOICES = ["rock", "paper", "scissors"]
WIN_LOGIC = (["rock", "scissors"], ["paper", "rock"], ["scissors", "paper"])

player1_choice = input("Choose for P1:")
player2_choice = input("choose for P2:")
choices = [player1_choice, player2_choice]

if choices in WIN_LOGIC:
    print("player 1 wins")
else:
    print("player 2 wins")
