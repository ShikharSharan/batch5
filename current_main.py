import csv
import random
import string

# Function to create a new account
def create_account():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")
    initial_balance = float(input("Enter the initial balance: "))

    # Generating Account number, IFSC code, and Customer ID
    account_number = random.randint(1000000000, 9999999999)
    ifsc_code = "SBIN" + str(random.randint(1000, 9999))
    customer_id = (''.join(random.choices(string.ascii_uppercase, k=4)))+(''.join(random.choices(string.digits, k=4)))

    # Saving the account details in a CSV file
    with open('account_details.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, address, account_number, ifsc_code, customer_id, password,initial_balance])

    print("Your account has been created successfully!")
    print("Your account number is:", account_number)
    print("Your IFSC code is:", ifsc_code)
    print("Your Customer ID is:", customer_id)

# Function to login to an existing account
def login():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")

    with open('account_details.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == account_number and row[5] == password:
                print("Welcome,", row[0])
                return True

    print("Invalid account number or password")
    return False

# Function for deposit
def deposit():
    account_number = input("Enter your account number: ")
    amount = float(input("Enter the amount to deposit: "))

    with open('account_details.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for row in rows:
            if row[2] == account_number:
                balance = float(rows[rows.index(row)][6])
                balance += amount
                rows[rows.index(row)][6] = balance
                break

    with open('account_details.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Amount deposited successfully!")
    print("Your current balance is:", balance)

# Function for withdrawal
def withdraw():
    account_number = input("Enter your account number: ")
    amount = float(input("Enter the amount to withdraw: "))

    with open('account_details.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for row in rows:
            if row[2] == account_number:
                balance = float(rows[rows.index(row)][6])
                if balance >= amount:
                    balance -= amount
                    rows[rows.index(row)][6] = balance
                    with open('account_details.csv', mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(rows)
                    print("Amount withdrawn successfully!")
                    print("Your current balance is:", balance)
                else:
                    print("Insufficient balance")
                break

def transfer():
    sender_account_number = input("Enter your account number: ")
    recipient_account_number = input("Enter the recipient's account number: ")
    amount = float(input("Enter the amount to transfer: "))

    # read account details from file
    with open('account_details.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        sender_index = None
        recipient_index = None

        # find the sender and recipient accounts
        for i, row in enumerate(rows):
            if row[2] == sender_account_number:
                sender_index = i
                sender_balance = float(row[6])
            elif row[2] == recipient_account_number:
                recipient_index = i
                recipient_balance = float(row[6])

        # check if both accounts were found
        if sender_index is None:
            print("Sender account not found")
            return
        elif recipient_index is None:
            print("Recipient account not found")
            return

        # check if sender has sufficient balance
        if sender_balance < amount:
            print("Insufficient balance")
            return

        # update the sender and recipient balances
        sender_balance -= amount
        recipient_balance += amount
        rows[sender_index][6] = sender_balance
        rows[recipient_index][6] = recipient_balance

        # save the updated account details to file
        with open('account_details.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Amount transferred successfully!")
        print("Your current balance is:", sender_balance)


def main():
    while True:
        print("Welcome to SBI Bank!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_account()
        elif choice == 2:
            if login():
                while True:
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. Logout")

                    option = int(input("Enter your option: "))

                    if option == 1:
                        deposit()
                    elif option == 2:
                        withdraw()
                    elif option == 3:
                        transfer()
                    elif option == 4:
                        break
                    else:
                        print("Invalid option!")
            else:
                continue
        elif choice == 3:
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice!")
            continue

main()


       
