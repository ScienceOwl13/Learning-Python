import random

def rollDice():
      diceResults.append(random.randint(1, diceType))

def rollAdvantage():
    for i in range(2):
        diceResults.append(random.randint(1, diceType))
    
    if diceResults[0] > diceResults[1]:
        print(f"\nYou rolled a {diceResults[0]} with advantage.")
    else:
        print(f"\nYou rolled a {diceResults[1]} with advantage.")


def rollDisadvantage():
    for i in range(2):
        diceResults.append(random.randint(1, diceType))
    
    if diceResults[0] < diceResults[1]:
        print(f"\nYou rolled a {diceResults[0]} with disadvantage.")
    else:
        print(f"\nYou rolled a {diceResults[1]} with disadvantage.")


diceType = int(input("What type of dice would you like to roll? d"))
diceQuantity = int(input("How many dice would you like to roll? "))
modifiers = input("Are you rolling with advantage, disadvantage, for a total or none? ")

diceNumRolled = 0
diceResults = []

if modifiers == "advantage":
    print(f"Okay, rolling a d{diceType} with advantage.")
    rollAdvantage()


elif modifiers == "disadvantage":
    print(f"Okay, rolling a d{diceType} with disadvantage.")
    rollDisadvantage()

elif modifiers == "total":
    print(f"Okay, rolling {diceQuantity}d{diceType}.")

    while diceNumRolled != diceQuantity:
        rollDice()
        diceNumRolled += 1
    print(f"The total of your roll is {sum(diceResults)}")

else:
    print(f"Okay, rolling {diceQuantity}d{diceType}.")

    while diceNumRolled != diceQuantity:
        rollDice()
        diceNumRolled += 1

print(f"\nYou rolled: {diceResults}")