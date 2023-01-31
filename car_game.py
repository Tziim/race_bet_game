import csv
import os
import pyfiglet
import pandas as pd
from colorama import Fore, Style


def reset_score():
    df = pd.read_csv("result.csv")
    blue_score = df.loc[0, "SCORE"]
    df.loc[0, "SCORE"] = (blue_score - blue_score)
    red_score = df.loc[1, "SCORE"]
    df.loc[1, "SCORE"] = (red_score - red_score)
    df.to_csv("result.csv", index=False)


def clear():
    os.system('cls')


clear()
car_race = pyfiglet.figlet_format("Car race", font="slant")
scoreboard = pyfiglet.figlet_format("Scoreboard", font="slant")
good_bye = pyfiglet.figlet_format("Have a nice day", font="slant")
wallet_text = pyfiglet.figlet_format("Wallet", font="slant")
bet_text = pyfiglet.figlet_format("Bet winner", font="slant")
error = Fore.RED + "Choose right number!" + Style.RESET_ALL
print(car_race)

# Choose action!
operations = ["1. Race",
              "2. Scoreboard",
              "3. Wallet",
              "4. Quit"]
wallet_operations = ["\n1. Add money to your account",
                     "2. Withdraw money",
                     "3. Back to menu"]
print(*operations, sep="\n")
operation_choice = input("Choose action 1 to 4: ")

while not operation_choice.isnumeric() \
        or int(operation_choice) > int(4) \
        or int(operation_choice) == int(0):
    print(error)
    operation_choice = input("Choose action 1 to 4: ")

# Race
while operation_choice == str(1):
    exec(open('track.py').read())

# Scoreboard
if operation_choice == str(2):
    clear()
    print(scoreboard)

    with open("result.csv", "r") as file:
        csvreader = csv.reader(file, delimiter=',')
        for score in csvreader:
            print(*score)

    print('\nType "RESET" to reset score!')
    menu = input("Press any key to continue!: ")
    while menu == "RESET":
        reset_score()
        clear()
        print(scoreboard)
        with open("result.csv", "r") as file:
            csvreader = csv.reader(file, delimiter=',')
            for score in csvreader:
                print(*score)
        print('\nType "RESET" to reset score!')
        menu = input("Press any key to continue!: ")
    else:
        exec(open('car_game.py').read())

# Wallet
elif operation_choice == str(3):
    exec(open('wallet.py').read())

# Quit
elif operation_choice == str(4):
    clear()
    print(good_bye)
    exit()
