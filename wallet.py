from car_game import clear, wallet_operations, wallet_text, error
from time import sleep
import csv
import pandas as pd
from colorama import Fore, Style

clear()
print(wallet_text)

with open("wallet.csv", "r") as file:
    csvreader = csv.reader(file, delimiter=',')
    for balance in csvreader:
        print(*balance)

print(*wallet_operations, sep="\n")
wallet_operations_choice = input("Choose operation 1 to 3: ")
while not wallet_operations_choice.isnumeric() \
        or int(wallet_operations_choice) > int(3) \
        or int(wallet_operations_choice) == int(0):
    print(error)
    wallet_operations_choice = input("Choose operation 1 to 3: ")

else:

    # Add money to your account!
    if wallet_operations_choice == str(1):
        clear()
        print(wallet_text)
        add_money = input(
            "How much money do you want to load into the account?: ")
        while not add_money.isnumeric():
            print(Fore.RED +
                  "Choose right amount of money or don't mess with cents!"
                  + Style.RESET_ALL)
            add_money = input(
                "How much money do you want to load into the account?: ")
        else:
            add_money = int(add_money)
            df = pd.read_csv("wallet.csv")
            balance = df.loc[0, "ACCOUNT BALANCE"]
            df.loc[0, "ACCOUNT BALANCE"] = (balance + add_money)
            df.to_csv("wallet.csv", index=False)
            print(Fore.BLUE + f"{add_money}$ added to your account!"
                  + Style.RESET_ALL)
            sleep(2)
            clear()
            print(wallet_text)
            exec(open('wallet.py').read())

    # Withdraw money!
    if wallet_operations_choice == str(2):
        clear()
        print(wallet_text)
        remove_money = input("How much money do you want to withdraw?: ")
        while not remove_money.isnumeric():
            print(Fore.RED +
                  "Choose right amount of money or don't mess with cents!"
                  + Style.RESET_ALL)
            remove_money = input("How much money do you want to withdraw?: ")
        else:
            df = pd.read_csv("wallet.csv")
            balance = df.loc[0, "ACCOUNT BALANCE"]
            while not remove_money.isnumeric() or balance < int(remove_money):
                print(Fore.RED +
                      "You don't have that much money or you didn't"
                      " enter valid number!"
                      + Style.RESET_ALL)
                remove_money = input(
                    "How much money do you want to withdraw?: ")

            else:
                remove_money = int(remove_money)
                df.loc[0, "ACCOUNT BALANCE"] = (balance - remove_money)
                df.to_csv("wallet.csv", index=False)
                print(Fore.BLUE +
                      f"{remove_money}$ has been withdrawn from your account!"
                      + Style.RESET_ALL)
                sleep(2)
                clear()
                print(wallet_text)
                exec(open('wallet.py').read())

    # Back to menu!
    if wallet_operations_choice == str(3):
        exec(open('car_game.py').read())
