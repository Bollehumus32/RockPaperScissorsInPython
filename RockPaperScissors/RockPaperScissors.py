import random

#Program for playing Rock Paper Scissors, with a custom number of rounds!

RoundsLeft = int(input('How many rounds will be played?: \n'))

Choices = ['Rock', 'Paper', 'Scissors']

ComputersPoints = 0

PlayersPoints = 0

while RoundsLeft > 0:
    PlayersPick = input('What do you wish to pick(Rock, Paper, Scissors):\n')

    #Running random int to decide computers pick for Rock (0), Paper(1) or Scissors(2)
    randNum = random.randint(0,2)
    ComputersPick = Choices[randNum]


    if PlayersPick in Choices:
        #First iteration for Scissors
        if PlayersPick == 'Rock' and ComputersPick == 'Scissors':
            print('Player Wins!')
            PlayersPoints += 1
        if PlayersPick == 'Paper' and ComputersPick == 'Scissors':
            print('Computer Wins!')
            ComputersPoints += 1
        if PlayersPick == 'Scissors' and ComputersPick == 'Scissors':
            print('Tie!')
            continue

        #Second iteration for Paper
        if PlayersPick == 'Rock' and ComputersPick == 'Paper':
            print('Computer Wins!')
            ComputersPoints += 1
        if PlayersPick == 'Paper' and ComputersPick == 'Paper':
            print('Tie!')
            continue
        if PlayersPick == 'Scissors' and ComputersPick == 'Paper':
            print('Player Wins!')
            PlayersPoints += 1

        #Third iteration for Rock
        if PlayersPick == 'Rock' and ComputersPick == 'Rock':
            print('Tie!')
            continue
        if PlayersPick == 'Paper' and ComputersPick == 'Rock':
            print('Player Wins!')
            PlayersPoints += 1
        if PlayersPick == 'Scissors' and ComputersPick == 'Rock':
            print('Computer Wins!')
            ComputersPoints += 1
    RoundsLeft -= 1
        #Done

    else:
        print('Invalid Input')

print(f'Players Score: {PlayersPoints}!')
print(f'Computers Score: {ComputersPoints}!')

#Winner Deciding:
if PlayersPoints > ComputersPoints:
    print('The Player Wins!')
else:
    print('The Computer Wins!')






