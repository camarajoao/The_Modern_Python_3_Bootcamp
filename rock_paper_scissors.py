import random

rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"


def play():
    player1 = input("player 1 chooses: ").lower()
    if player1 != 'rock' and player1 != 'paper' and player1 != 'scissors':
        print('invalid')
        play()
    else:
        print(computer)
        if player1 == computer:
                print("It's a tie! Play again")
        elif player1 == 'rock' and computer == 'scissors' or player1 == 'paper' and computer == 'rock' or player1 == 'scissors' and computer == 'paper':
                print("Player 1 wins")
        else:
                print("Computer 2 wins")

play()