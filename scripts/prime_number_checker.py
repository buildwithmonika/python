# Checks number is prime or not

import math

print("==== Welcome to the Prime Number Checker ====")


def is_prime(number):
    if number == 1:
        return False
    
    for x in range(2, int(math.sqrt(number)) + 1):
        if number % x == 0:
            return False
    
    return True
    

while True:
    while True:
        try:
            number = int(input("Enter a positive number: ").strip())
            if number > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a positive number.")
    
    if is_prime(number):
        print(f"{number} is a PRIME number.")
    else:
        print(f"{number} is NOT a prime number.")

    if input("Enter q/Q to quit or press any to continue: ").strip().lower() == "q":
        print("Thanks for using the Prime Number Checker!")
        break



