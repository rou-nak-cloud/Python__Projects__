import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS_COUNT_SLOT = 3
COLS_COUNT_SLOT = 3

symbol_count = {
    "A": 3,
    "B": 4,
    "C": 6,
    "D": 8,
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] # Get the symbol in the first column for the current line
        for column in columns:
            symbol_to_check = column[line] # Get the symbol in the current column for the current line
            if symbol != symbol_to_check: # If symbols don't match, break out of the loop
                break
        else:
            winnings += values[symbol] * bet # Calculate winnings if all symbols match
            winning_lines.append(line + 1) # Store the winning line (1-indexed)
    return winnings, winning_lines # Return total winnings and list of winning lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # Populate symbol_count list based on symbol counts get the key value
        for _ in range(symbol_count): # Add each symbol to the list as many times as its count
            all_symbols.append(symbol) # Add symbol to the all_symbol list

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:] # Create a copy of all_symbols to manipulate for this column
        for row in range(rows):
            value = random.choice(current_symbols) # Randomly select a symbol from the current symbols
            current_symbols.remove(value) # Remove the selected symbol to avoid duplicates in the same column
            column.append(value) # Add the selected symbol to the current column
            
        columns.append(column) # Add the completed column to the list of columns
    return columns # Return the generated slot machine columns

def print_slot_machine(columns):
    for row in range(len(columns[0])): # Iterate through each row index
        for i, column in enumerate(columns): # Iterate through each column with its index
            if i != len(columns) - 1: # If it's not the last column
                print(column[row], end=" | ") # Print the symbol with a separator
            else:
                print(column[row], end="") # Print the last symbol without a separator
        print() # Move to the next line after printing all columns for the current row



def deposit():
    while True:
        amount = input("Enter the amount you would like to deposit: ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? ({MIN_BET}-{MAX_BET}): ₹")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ₹{MIN_BET} - ₹{MAX_BET}.")
        else:
            print("Please enter a valid amount.")
    return amount


def spin(balance):
    lines = get_number_of_lines() 
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is: ₹{balance}")
        else:
            break

    print(f"You have deposited: ₹{balance}")
    print(f"You are betting ₹{bet} on {lines} lines. Total bet is: ₹{total_bet}")
    
    slots = get_slot_machine_spin(ROWS_COUNT_SLOT, COLS_COUNT_SLOT, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ₹{winnings}.")
    print(f"You won on lines:", *winning_lines)
    
    return winnings - total_bet

def main_game():
    print("Welcome to the Slot Machine!")
    balance = deposit()
    while True:
        print(f"Your current balance is ₹{balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer.lower() == "q":
            break
        balance += spin(balance)
    print(f"You left with ₹{balance}")


main_game()
    