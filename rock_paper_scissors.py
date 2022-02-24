#Have it so that the if it's a tie breaking round, the game uses a different function, so that if you put in a unsupported option it will re-do the match in the tie breaking round format.
#Currently, the tieBreakingRound() function doesn't do anything, it needs to include everything that is in playRockPaperScissors().
#Figuire out a way to enable/disable isTieBreakingRound, so if that's true, it will reroute the error messages from normal to the tie breaking round version.

import random
from time import sleep


tieGame = input("Welcome to Connor's Rock, Paper, Scissors Game. ")
numOfRounds = int(input("How many games would you like to play? "))

roundsPlayed = 0

playerScore = 0
computerScore = 0

isTieBreakingRound = bool


def playRockPaperScissors():
    
    global playerScore
    global computerScore
    global isTieBreakingRound

        #Chooses a number between 1 and 3. 1 is rock, 2 is paper, 3 is scissors.
    computerMove = random.randint(1,3)

    #Asks player to for their move
    playerMove = input("\nDo you choose rock, paper or scissors? ")

    #Determins who wins.

    #Computer Chooses Rock
        #Rock vs Rock
    if computerMove == 1 and playerMove == "rock":
        print("You chose: 'rock' and the computer chose 'rock'. No one gets a point.")
        print("Redoing this match.")
        playRockPaperScissors()

        #Rock vs Paper
    elif computerMove == 1 and playerMove == "paper":
        print("You chose: 'paper' and the computer chose: 'rock'. You win!")
        playerScore += 1
        print(f"You have {playerScore} and the computer has {computerScore}")

        #Rock vs Scissors
    elif computerMove == 1 and playerMove == "scissors":
        print("You chose: 'scissors' and the computer chose: 'rock'. The computer wins!")
        computerScore += 1
        print(f"You have {playerScore} and the computer has {computerScore}")

    #Computer Chooses Paper
        #Paper vs Rock
    elif computerMove == 2 and playerMove == "rock":
        print("You chose: 'rock' and the computer chose: 'paper'. The computer wins!")
        computerScore += 1
        print(f"You have {playerScore} and the computer has {computerScore}")

        #Paper vs Paper
    elif computerMove == 2 and playerMove == "paper":
        print("You chose: 'paper' and the computer chose: 'paper'. No one gets a point.")
        print("Redoing this match.")
        playRockPaperScissors()

        #Paper vs Scissors
    elif computerMove == 2 and playerMove == "scissors":
        print("You chose: 'scissors' and the computer chose: 'paper'. You win!")
        playerScore += 1
        print(f"You have {playerScore} and the computer has {computerScore}")

    #Computer Chooses Scissors
        #Scissors vs Rock
    elif computerMove == 3 and playerMove == "rock":
        print("You chose: 'rock' and the computer chose: 'scissors'. You win!")
        playerScore += 1
        print(f"You have {playerScore} and the computer has {computerScore}")

        #Scissors vs Paper
    elif computerMove == 3 and playerMove == "paper":
        print("You chose: 'paper' and the computer chose: 'Scissors'. The computer wins!")
        computerScore += 1
        print(f"You have {playerScore} and the computer has {computerScore}")

        #Scissors vs Scissors
    elif computerMove == 3 and playerMove == "scissors":
        print("You chose: 'scissors' and the computer chose: 'scissors'. No one gets a point.")
        print("Redoing this match.")
        playRockPaperScissors()

        #If wrong option is chosen and it's the tie-breaking round
    elif playerMove != "rock" or "paper" or "scissors" and isTieBreakingRound == True:
        TieBreakingRound()

        #If wrong option is chosen
    else:
        print(f"You chose: {playerMove}, which is not valid. Please choose either 'rock', 'paper' or 'scissors'.")
        print("Here is a redo of this round:")
        playRockPaperScissors()

def TieBreakingRound():

    global computerScore
    global playerScore

    input(f"\nThe scores are tied at {computerScore} for the computer and {playerScore} for you! Are you ready for the tie breaking round? ")

        #Chooses a number between 1 and 3. 1 is rock, 2 is paper, 3 is scissors.
    computerMove = random.randint(1,3)

    #Asks player to for their move
    playerMove = input("Do you choose rock, paper or scissors? ")

    #Determins who wins.

    #Computer Chooses Rock
        #Rock vs Rock
    if computerMove == 1 and playerMove == "rock":
        print("You chose: 'rock' and the computer chose 'rock'. No one gets a point.")
        print("Redoing this match.")
        playRockPaperScissors()

        #Rock vs Paper
    elif computerMove == 1 and playerMove == "paper":
        print("You chose: 'paper' and the computer chose: 'rock'. You win!")
        playerScore += 1
        print(f"You have {playerScore} and the computer has {computerScore}")

        #Rock vs Scissors
    elif computerMove == 1 and playerMove == "scissors":
        print("You chose: 'scissors' and the computer chose: 'rock'. The computer wins!")
        computerScore += 1
        print(f"You have {playerScore} and the computer has {computerScore}")

    #Computer Chooses Paper
        #Paper vs Rock
    elif computerMove == 2 and playerMove == "rock":
        print("You chose: 'rock' and the computer chose: 'paper'. The computer wins!")
        computerScore += 1
        print(f"You have {playerScore} and the computer has {computerScore}")

        #Paper vs Paper
    elif computerMove == 2 and playerMove == "paper":
        print("You chose: 'paper' and the computer chose: 'paper'. No one gets a point.")
        print("Redoing this match.")
        playRockPaperScissors()

        #Paper vs Scissors
    elif computerMove == 2 and playerMove == "scissors":
        print("You chose: 'scissors' and the computer chose: 'paper'. You win!")
        playerScore += 1
        print(f"You have {playerScore} and the computer has {computerScore}")

    #Computer Chooses Scissors
        #Scissors vs Rock
    elif computerMove == 3 and playerMove == "rock":
        print("You chose: 'rock' and the computer chose: 'scissors'. You win!")
        playerScore += 1
        print(f"You have {playerScore} and the computer has {computerScore}")

        #Scissors vs Paper
    elif computerMove == 3 and playerMove == "paper":
        print("You chose: 'paper' and the computer chose: 'Scissors'. The computer wins!")
        computerScore += 1
        print(f"You have {playerScore} and the computer has {computerScore}")

        #Scissors vs Scissors
    elif computerMove == 3 and playerMove == "scissors":
        print("You chose: 'scissors' and the computer chose: 'scissors'. No one gets a point.")
        print("Redoing this match.")
        playRockPaperScissors()

        #If wrong option is chosen and it's the tie-breaking round
    elif playerMove != "rock" or "paper" or "scissors" and isTieBreakingRound == True:
        print("\nYou have typed in something that is not an option. You get to try again:")
        TieBreakingRound()

        #If wrong option is chosen
    else:
        print(f"You chose: {playerMove}, which is not valid. Please choose either 'rock', 'paper' or 'scissors'.")
        print("Here is a redo of this round:")
        playRockPaperScissors()


#Stuff that needs to be in here for the game

if numOfRounds == 0:
    print(f"You have selected to play 0 rounds. Quitting the game.")
    sleep(3)
    quit()


while numOfRounds != roundsPlayed:

    playRockPaperScissors()
    roundsPlayed += 1

if playerScore == computerScore:
    isTieBreakingRound = True
    TieBreakingRound()
    isTieBreakingRound = False
    

if playerScore < computerScore:
    print(f"\nYou lost. The computer won. The score was {computerScore} - {playerScore} for the computer.")
else:
    print(f"\nYou won. The computer lost. The score was {playerScore} - {computerScore} for you.")

print("\nThank you for playing Rock, Paper, Scissors.")

#Secret developer settings:

#At the very first prompt, put "*" to make the round a tie breaking round. You need to answer "1" for the amount of rounds, then get the first prompt wrong.
if tieGame == "*":
    isTieBreakingRound = True

sleep(5)

exit()