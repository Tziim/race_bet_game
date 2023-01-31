import random
from time import *
import pyfiglet
import time
import pandas as pd
from car_game import bet_text, error, clear
from colorama import Fore, Style

# Ready... Set... GO!!!
ready = pyfiglet.figlet_format("READY . . .")
set_ = pyfiglet.figlet_format("SET . . .")
go = pyfiglet.figlet_format("GO ! ! !")

clear()

# Make bet
print(bet_text)
bet = input("Make your bet for winner! Blue(1)/Red(2): ")
while not bet.isnumeric() \
        or int(bet) > int(2) \
        or int(bet) == int(0):
    print(error)
    bet = input("Make your bet for winner! Blue(1)/Red(2): ")
bet = int(bet)

# Make price of bet
bet_price = input("Make your bet price: ")

# Account balance
df = pd.read_csv("wallet.csv")
balance = df.loc[0, "ACCOUNT BALANCE"]

while not bet_price.isnumeric() \
        or int(bet_price) > int(balance):
    print(Fore.RED + "You don't have that much money or you didn't enter"
                     " valid number!" + Style.RESET_ALL)
    bet_price = input("Make your bet price: ")

# Remove money from account
bet_price = int(bet_price)
df.loc[0, "ACCOUNT BALANCE"] = (balance - bet_price)
df.to_csv("wallet.csv", index=False)

# Ready... Set... GO!!!
clear()
print(ready)
sleep(1)
clear()
print(set_)
sleep(1)
clear()
print(go)
sleep(1)
clear()

# Race
blue_car = [Fore.BLUE + "CAR" + Style.RESET_ALL]
red_car = [Fore.RED + "CAR" + Style.RESET_ALL]
track_length = random.randint(10, 25)

length_blu = len(blue_car)
length_red = len(red_car)

race_time = time.time()
for race in range(track_length):
    road_blu = random.randint(1, 3) * " "
    road_red = random.randint(1, 3) * " "
    time.sleep(0.2)
    blue_car.insert(0, road_blu)
    red_car.insert(0, road_red)
    clear()
    print(pyfiglet.figlet_format("Race", font="slant"))
    print(f"{' '.join(map(str, blue_car))}\n"
          f"{' '.join(map(str, red_car))}")

clear()

race_time = time.time() - race_time
print(pyfiglet.figlet_format("Race over", font="slant"))
print(f"{' '.join(map(str, blue_car))}\n"
      f"{' '.join(map(str, red_car))}")
print(f"RACE TIME: {'{:.2f}'.format(race_time)} sec")

blue_speed = (blue_car.count(" ")) + \
             (blue_car.count("  ") * 2) + \
             (blue_car.count("   ") * 3)
red_speed = (red_car.count(" ")) + \
            (red_car.count("  ") * 2) + \
            (red_car.count("   ") * 3)

# SCORE

blue_car_won = pyfiglet.figlet_format("BLUE CAR WON", font="slant")
red_car_won = pyfiglet.figlet_format("RED CAR WON", font="slant")
tie = pyfiglet.figlet_format("TIE", font="slant")

if blue_speed > red_speed:
    print(blue_car_won)
    # Add score points
    df = pd.read_csv("result.csv")
    score = df.loc[0, "SCORE"]
    df.loc[0, "SCORE"] = (score + 1)
    df.to_csv("result.csv", index=False)

    # Add money to account if bet was right
    if bet == int(1):
        print(Fore.BLUE + f"Your bet was {bet_price}$ on Blue car. You win"
                          f" and doubled your money!" + Style.RESET_ALL)
        df = pd.read_csv("wallet.csv")
        balance = df.loc[0, "ACCOUNT BALANCE"]
        df.loc[0, "ACCOUNT BALANCE"] = (balance + (2 * bet_price))
        df.to_csv("wallet.csv", index=False)
    else:
        print(Fore.RED + f"Your bet was {bet_price}$ on Red car. You lose and"
                         f" lost your money!" + Style.RESET_ALL)

elif red_speed > blue_speed:
    print(red_car_won)
    # Add score points
    df = pd.read_csv("result.csv")
    score = df.loc[1, "SCORE"]
    df.loc[1, "SCORE"] = (score + 1)
    df.to_csv("result.csv", index=False)

    # Add money to account if bet was right
    if bet == int(2):
        print(Fore.BLUE + f"Your bet was {bet_price}$ on Red car. You win and"
                          f" doubled your money!" + Style.RESET_ALL)
        df = pd.read_csv("wallet.csv")
        balance = df.loc[0, "ACCOUNT BALANCE"]
        df.loc[0, "ACCOUNT BALANCE"] = (balance + (2 * bet_price))
        df.to_csv("wallet.csv", index=False)
    else:
        print(Fore.RED + f"Your bet was {bet_price}$ on Blue car. You lose and"
                         f" lost your money!" + Style.RESET_ALL)

elif red_speed == blue_speed:
    print(tie)

    # Get your money back
    if bet == int(1) or int(2):
        print(Fore.BLUE + f"Your bet was {bet_price}$. It was a tie, "
                          f" you got your money back." + Style.RESET_ALL)
        df = pd.read_csv("wallet.csv")
        balance = df.loc[0, "ACCOUNT BALANCE"]
        df.loc[0, "ACCOUNT BALANCE"] = (balance + bet_price)
        df.to_csv("wallet.csv", index=False)

# Play again
race_again = input("Race again? Yes(1)/No(random key): ")
if race_again != str(1):
    exec(open('car_game.py').read())
