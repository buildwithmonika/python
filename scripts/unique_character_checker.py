print("==== Welcome to the Checker ====")

def unique_character_checker(text: str) -> None:
    seen = set() # holds unique elements, complexity is O(1)
    for ch in text:      
        if ch in seen:
            print(f"Duplicate '{ch}' found.")
            return
        seen.add(ch)
    print("No duplicate character found.")

while True:
    user_input = input("Enter a string: ").lower()
    unique_character_checker(user_input)

    if input("Enter any key to continue or Q/q to exit: ").lower() == "q":
        break