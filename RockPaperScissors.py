
import random

#  1 = rock
#  2 = paper
#  3 = scissors


# Generates random object(rock,paper,scissors)
for x in range(1):
    object1 = random.randint(1,3)
player1 = object1

for y in range(1):
    object2 = random.randint(1,3)
player2 = object2


# Player choose
player3 = input("Enter your object: ")
if player3.lower() in "rock":
    player3 = 1
elif player3.lower() in "paper":
    player3 = 2
elif player3.lower() in "scissors":
    player3 = 3
else:
    print("Invalid object")



# Condition of lose
if player3 == 1 and (player2 == 2 or player1 == 2):
    print("Lose")
elif player3 == 2 and (player2 == 3 or player1 == 3):
    print("Lose")
elif player3 == 3 and (player2 == 1 or player1 == 1):
    print("Lose")

# Condition of win
if player3 == 1 and player2 == 3 and player1 == 3:
    print("Win")
elif player3 == 2 and player2 == 1 and player1 == 1:
    print("Win")
elif player3 == 3 and player2 == 2 and player1 == 2:
    print("Win")

# Condition of draw
elif player3 == 1:
    if player2 == 1 or player1 == 1:
        print("Draw")
elif player3 == 2:
    if player2 == 2 or player1 == 2:
        print("Draw")
elif player3 == 3:
    if player2 == 3 or player1 == 3:
        print("Draw")


# To see result
print(player3)
print(player2)
print(player1)