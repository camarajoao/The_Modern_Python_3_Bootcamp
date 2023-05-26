import random

# for x in range(1,10, 2):
#     print(x)

# x = 0
# for num in range(10, 21):
#     if num % 2 != 0:
#         x += num
# print(x)

# question = input('How many times do I have to tell you? ')
# for x in range(int(question)):
#     print('Clean up your room!')

##loop through 1-20 and print the following:
##if the number is 4 or 13, print UNLUCKY!
##if the number is even, print even. if the number is odd, print odd
# for x in range(1,21):
#     if x == 4 or x == 13:
#         print('UNLUCKY!')
#     elif x % 2 == 0:
#         print('even')
#     else:
#         print('odd')

##smiley face exercise
# x = 1
# while x < 11:
#     print(("\U0001f600")*x)
#     x+=1

##stop copying me exercise
# user = input("Hey how's it going? ")
# while user != "stop copying me":
#     print(user)
#     user = input()

# number = 0
# i = 0
# while number != 5:
#     i += 1
#     number = random.randint(1,10)
# print(i)


#guessing game
x = random.randint(1,10)
guess = None

while guess != x:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if guess < x:
        print("too low. Try again ")
    elif guess > x:
        print("too high. Try again ")
    else:
        print("You guessed it!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            x = random.randint(1,10)
            guess = None
        else:
            print("Thank you for playing!")
            break