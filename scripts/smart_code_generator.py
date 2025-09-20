# smart_code_generator.py
# Generates a custom username, lucky ID, and fun code based on your name, birth year, and favorite number.

import random

def username(full_name, fav_number):
    return f"{full_name.lower().replace(' ', '')}_{fav_number}"

def lucky_id(full_name, fav_number):
    return f"{full_name[0].upper()}{fav_number}{full_name[-1].upper()}"

fun_emojis = ["🎉", "🚀", "✨", "🍀", "🔥", "😎", "🌈"]

def smart_code(birth_year, fav_number):
    code = (int(birth_year[-2:]) + int(fav_number)) * 2
    return code

print("==== Welcome to the Smart Code Generator ====")

while True: 
    while True:
        full_name = input("Enter your full name: ").strip()
        if all(char.isalpha() or char.isspace() for char in full_name) and len(full_name) > 0:
            break
        print("Please enter a valid name using letters and spaces only.")

    while True: 
        birth_year = input("Enter your birth year: ").strip()
        if birth_year.isdigit():
            break
        print("Please enter numberic value e.g. 1998")

    while True:
        fav_number = input("Enter your favorite number: ").strip()
        if fav_number.isdigit():
            break
        print("Please enter positive numeric value e.g. 56")

   
    random_emoji = random.choice(fun_emojis)
    print(f"""Great! Here is your generated info: 
        Username: {username(full_name, fav_number)}
        Lucky ID: {lucky_id(full_name, fav_number)}
        Code: {smart_code(birth_year, fav_number)}{random_emoji}
    """)

    is_continue = input("Enter q/Q to quit or random character to continue: ").strip().lower()
    match is_continue:
        case 'q': 
            print("Good Bye!")
            break
        case _:
            pass

