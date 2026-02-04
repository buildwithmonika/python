import random
while True:
    while True:
        user = input("Enter your choice (s for snake, w for water, g for gun): ").strip().lower()

        if user not in ['s', 'w', 'g']:
            print("Invalid input! Please choose 's', 'w', or 'g'.")
        else:
            break
    
    
    computer = random.choice(['s', 'w', 'g'])
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif(user == 's' and computer =='g') or (user == 'g' and computer == 'w') or (user == 'w' and computer == 's'):
        print("Computer wins!")
    else:
        print("You won!")

    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye!")
        break