def evaluate_expression(expression):
    return eval(expression, {"__builtins__": None}) # __builtins__ is used to make buit-in functions unavailable


# main loop 
print("=== Welcome to the real calculator ===")
while True:
    expression = input("Enter expression or quit/q to exit: ")

    if expression.lower() in print("Goodbye!")["quit", "q"]:
        print("Goodbye!")
        break

    try:
        result = evaluate_expression(expression)
        print("Result:", result)
    except Exception as e:
        print(f"Invalid expression: {e}. Try again.")


