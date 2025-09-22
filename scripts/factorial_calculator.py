# Calculates factorial of a number

print("==== Welcome to the Factorial Calculator ====")


def factorial(number):
    if number <= 1:
        return 1
    
    return number * factorial(number-1)


while True: 
    while True:
        try:
            number = int(input("Enter a number: "))
            if number >= 0:
                break
            print("Please enter a non-negative number.")

        except ValueError:
            print("Invalid input. Please enter a whole number(>= 0).")

    print(f"Factorial of {number} is: {factorial(number)}")

    if input("Enter q to quit or any key to continue: ").strip().lower() == "q":
        print("==== Good Bye! ====")
        break

