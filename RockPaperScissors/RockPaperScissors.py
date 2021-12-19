import random

RoundsLeft = int(input('How many rounds will be played?: \n'))

Choices = ['Rock', 'Paper', 'Scissors']

ComputersPoints = 0

PlayersPoints = 0

while RoundsLeft >= 0:
    PlayersPick = input('What do you wish to pick(Rock, Paper, Scissors)')

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
        #Done
        else:
            print('Invalid Input')





