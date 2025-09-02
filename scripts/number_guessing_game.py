import random

def number_generator():
    return random.randint(1, 100)

def verify_number(number, guess):
    diff = (number - guess)
    threshhold = 10
    if guess < number:
        if diff > threshhold:
            print("Too low! Try again.")
        else: 
            print("Low but close! Try again.")
    else:
        if diff > threshhold:
            print("Too high! Try again.")
        else:
            print("High but close! Try again.")
            

# main function 

print("""
===== Welcome to the Number Guessing Game ====
I'll select a number between 1 & 100. can you guess it?
""")

while True:
    is_continue = input("To continue enter y/Y or q/Q to quit: ").lower()

    match is_continue:
        case "y":
            number = number_generator()
            counter = 0
            while True:
                try:
                    guess = int(input("Enter your guess: "))
                except ValueError:
                    print("Please enter valid number.")
                    continue
                counter += 1
                if guess == number:
                    print(f"Correct! you guessed it in {counter} tries!")
                    break
                else:
                    verify_number(number, guess)
        case "q":
            print("Good Bye!")
            break
        case _:
            print("Please enter valid input.")
            


