#===== CLI Calculator =====

# Functions
def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result -= n
    return result

def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

def divide(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        if n == 0:
            return "Error: Division by zero!"
        result /= n
    return result

# Main loop
while True:
    operation = input("""
        =========== Calculator ==========
        Select operation: 
        1. Add(+)
        2. Subtract(-)
        3. Multiply(*)
        4. Divide(/)
        5. Exit
        Enter choice: """)

    if operation == "5":
        print("Exiting calculator. Goodbye!")
        break

    numbers_input = input("Enter numbers separated by space: ")
    try:
        numbers = [float(n) for n in numbers_input.split()]
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    match operation:
        case "1":
            output = add(numbers)
        case "2":
            output = subtract(numbers)
        case "3":
            output = multiply(numbers)
        case "4":
            output = divide(numbers)
        case _:
            print("Invalid choice! Try again.")
            continue

    print("Output:", output)