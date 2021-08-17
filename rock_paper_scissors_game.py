print("...rock...\n")
print("...paper...\n")
print("...scissors...\n")
player1Inp = input("enter player 1's choice: \n")
player2Inp = input("enter player 2's choice: \n")
print("SHOOT!\n")

if player1Inp == "rock" and player2Inp == "scissors":
    print("Player1 wins")
elif player1Inp == "scissors" and player2Inp == "paper":
    print("Player1 wins")
elif player1Inp == "paper" and player2Inp == "rock":
    print("Player1 wins")

elif player1Inp == "rock" and player2Inp == "rock":
    print("Tie")
elif player1Inp == "paper" and player2Inp == "paper":
    print("Tie")
elif player1Inp == "scissors" and player2Inp == "scissors":
    print("Tie")
else:
    print("Player2 wins")