import random

def balance(bal, bet, color, pick):
    # check if the user's pick matches the winning color
    if pick == color:
        print("bet won, ur bet was doubled")
        bal += bet * 2
    elif pick != color:
        print("bet lost")
        bal -= bet
    return bal

colours = ["red", "black"]

bal = 100  # initial balance

while True:
    print("gambling game")
    color = random.choice(colours)  # randomly choose the winning color
    bet = int(input("enter ur bet: "))
    pick = input("pick colour (red/black): ")

    print(f"the winning color was: {color}")  # show the winning color for better user experience

    bal = balance(bal, bet, color, pick)  # update balance based on result
    print("Your current balance is:", bal)

    if bal <= 0:
        print("you've run out of money. game over.")
        break

    count = input("wanna play again?? (y/n): ")
    if count == "y":
        continue
    elif count == "n":
        break
    else:
        print("error")
        continue
