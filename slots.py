from random import choice
from time import sleep
import sys

def calculate_win(r1, r2, r3, bet_multiplier=1):
    win_map = {
        "🍌": 20,
        "🍒": 20,
        "🍋": 20,
        "🍉": 20,
        "🍇": 20,
        "⭐": 100,
        "🔔": 100,
        "🍀": 100,
        "💎": 150
    }
    
    if r1 == r2 == r3:
        return win_map.get(r1, 0) * bet_multiplier
    return 0

def all_in_roll(bet, time_stamp):
    global balance, tries
    
    if bet > balance:
        print(f"ERROR4: Bet {bet} exceeds balance {balance}.")
        return
    
    balance -= bet
    tries += 1
    sleep(time_stamp)
    
    r1, r2, r3 = choice(possibilities), choice(possibilities), choice(possibilities)
    
    win = calculate_win(r1, r2, r3, bet)
    
    if win > 0:
        balance += win + bet
        if win >= 100 * bet:
            print("MEGA BIG WIN")
        else:
            print("BIG WIN")
    
    print(f"{r1} {r2} {r3} {balance}")

def single_roll():
    global balance
    
    try:
        bet = int(input("Bet: "))
        
        if bet > balance:
            print("ERROR4: Not enough balance")
            return
        
        balance -= bet
        
        r1, r2, r3 = choice(possibilities), choice(possibilities), choice(possibilities)
        
        win = calculate_win(r1, r2, r3, bet)
        
        if win > 0:
            balance += win + bet
            if win >= bet * 100:
                print("MEGA BIG WIN")
            else:
                print("BIG WIN")
        
        print(f"{r1} {r2} {r3} {balance}")
    
    except ValueError:
        print("ERROR1: Invalid input. Please enter a number.")

# Main game loop
balance = 1000
is_active = True
possibilities = ["💎", "🍀", "🔔", "⭐", "🍇", "🍇", "🍉", "🍉", "🍋", "🍋", "🍒", "🍒", "🍌", "🍌"]
tries = 0

while is_active:
    print("1. Single roll")
    print("2. Death roll")
    
    try:
        x = int(input("x: "))
        
        if x == 1:
            single_roll()
        elif x == 2:
            try:
                bet = int(input("Place bet: "))
                time_stamp = float(input("Time delay: "))
                
                if time_stamp <= 0:
                    print("ERROR5: Time delay must be a positive number.")
                    continue
                
                while balance > 0:
                    all_in_roll(bet, time_stamp)
            
                sys.exit(f"YOU LOSE AFTER {tries} TRIES")
            except ValueError:
                print("ERROR2: Invalid input for bet or time delay.")
        else:
            print("ERROR3: Invalid option. Please choose 1 or 2.")
    
    except ValueError:
        print("ERROR1: Invalid input. Please enter a number.")
        break
