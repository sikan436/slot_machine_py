current_balance = 0
previous_balance = 0

while True:
    try:
        amount = float(input("Enter amount to deposit (type 'n' to stop): "))
        if amount == 0:
            continue
        if amount < 0:
            print("Please enter a positive amount.")
            continue
        
        previous_balance = current_balance  # Store previous balance
        current_balance += amount
        
        print(f"Previous Balance: {previous_balance}")
        print(f"Current Balance: {current_balance}")
    
    except ValueError:
        print("Invalid input. Please enter a number or 'n' to stop.")

    choice = input("Do you want to continue depositing? (y/n): ")
    if choice.lower() != 'y':
        break

print("Exiting the program.")
