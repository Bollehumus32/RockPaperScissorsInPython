import random

#Program for playing Rock Paper Scissors, with a custom number of rounds!

RoundsLeft = int(input('How many rounds will be played?: \n'))

Choices = ['rock', 'paper', 'scissors']
#While loop to run program until user quits.
while True:

    ComputersPoints = 0

    PlayersPoints = 0

    #While loop to run program til there are no rounds left.
    while RoundsLeft > 0:
            RoundsInvert = RoundsLeft - 1 #Used instead of having RoundsLeft - (RoundsLeft - 1) ->
                                          #to make for more readable code.

            print(f'---------Round Number: {RoundsLeft - RoundsInvert}---------\n')

            PlayersPick = input('What do you wish to pick(rock, paper, scissors):\n').lower()

            #Running random int to decide computers pick for Rock (0), Paper(1) or Scissors(2)
            randNum = random.randint(0,2)
            ComputersPick = Choices[randNum]

            #Running actual program:
            if PlayersPick in Choices:
                #First iteration for Scissors
                if PlayersPick == 'rock' and ComputersPick == 'scissors':
                    print('Player Wins!\n')
                    PlayersPoints += 1
                if PlayersPick == 'paper' and ComputersPick == 'scissors':
                    print('Computer Wins!\n')
                    ComputersPoints += 1
                if PlayersPick == 'scissors' and ComputersPick == 'scissors':
                    print('Tie!\n')
                    pass

                #Second iteration for Paper
                if PlayersPick == 'rock' and ComputersPick == 'paper':
                    print('Computer Wins!\n')
                    ComputersPoints += 1
                if PlayersPick == 'paper' and ComputersPick == 'paper':
                    print('Tie!\n')
                    pass
                if PlayersPick == 'scissors' and ComputersPick == 'paper':
                    print('Player Wins!\n')
                    PlayersPoints += 1

                #Third iteration for Rock
                if PlayersPick == 'rock' and ComputersPick == 'rock':
                    print('Tie!\n')
                    pass
                if PlayersPick == 'paper' and ComputersPick == 'rock':
                    print('Player Wins!\n')
                    PlayersPoints += 1
                if PlayersPick == 'scissors' and ComputersPick == 'rock':
                    print('Computer Wins!\n')
                    ComputersPoints += 1

            RoundsLeft -= 1

            if PlayersPick not in Choices: 
                print('Invalid Input\n')
                #Done

    print(f'Players Score: {PlayersPoints}!\n')
    print(f'Computers Score: {ComputersPoints}!\n')

    #Winner Deciding:
    if PlayersPoints > ComputersPoints:
        print('The Player Wins!')
    elif PlayersPoints == ComputersPoints:
        print("It's a Tie!")
    else:
        print('The Computer Wins!')

    PlayAgain = input('Do you wish to play again? (Y/N)\n').lower()

    #Rerun program?
    if PlayAgain == 'y':
        continue
    elif PlayAgain == 'n': 
        break
    else: 
        print('Invalid Input')
        break
    






