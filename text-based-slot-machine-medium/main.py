MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


# Deposit here
def deposit():
    while True:
        amount = input("Enter your deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number. ")


    return amount

# getting total no of lines
def get_number_of_lines():
    while True:
        lines = input(f"Enter the no of lines to bet on (1 - {MAX_LINES}) ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print(f"Line must be in between 1 - {MAX_LINES}")
        else:
            print("Please enter a number. ")


    return lines

# Amount to bet on each line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet should be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number. ")


    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Your total bet is equal to: ${total_bet}")
main()