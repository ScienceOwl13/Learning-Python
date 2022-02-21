import random
from time import sleep


print("Welcome to Connor's Rock, Paper, Scissors Game.")
numOfRounds = int(input("How many games would you like to play? "))

roundsPlayed = 0

playerScore = 0
computerScore = 0


def playRockPaperScissors():
    
    global playerScore
    global computerScore

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

    #If wrong option is chosen
    else:
        print(f"You chose: {playerMove}, which is not valid.")


while numOfRounds != roundsPlayed:

    playRockPaperScissors()
    roundsPlayed += 1

if playerScore == computerScore:
    input("\nThe scores are tied! Are you ready for the tie breaking round? ")
    playRockPaperScissors()

if playerScore < computerScore:
    print(f"\nYou lost. The computer won. The score was {computerScore} - {playerScore} for the computer.")
else:
    print(f"\nYou won. The computer lost. The score was {playerScore} - {computerScore} for you.")

print("\nThank you for playing Rock, Paper, Scissors.")

sleep(10)

exit()