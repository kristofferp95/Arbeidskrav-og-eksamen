import random

computer = random.randint(0, 2)
print(f'0 = scissor / 1 = rock / 2 = paper')
user = int(input(f'Enter a number between 0 and 2: '))

if computer == 0:
    computerPicked = str("scissor")
elif computer == 1:
    computerPicked = str("rock")
else:
    computerPicked = str("paper")

if user == 0:
    userPicked = str("scissor")
elif user == 1:
    userPicked = str("rock")
else:
    userPicked = str("paper")

if (user == 0 and computer == 2
    or user == 1 and computer == 0 
    or user == 2 and computer == 1):
    result = str(". You win!")
elif (computer == 0 and user == 2
    or computer == 1 and user == 0
    or computer == 2 and user == 1):
    result = str(". Computer wins")
else: 
    result = str(". It is a Draw")


print(f'The computer picked {computerPicked} and you picked {userPicked}{result}')