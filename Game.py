import random

def guess_number():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if user_guess < target_number:
                print("Higher!")
            elif user_guess > target_number:
                print("Lower!")
            else:
                print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_number()
