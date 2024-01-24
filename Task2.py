import random

def play_game(player_choice, computer_choice):
    print(f"Player chooses {player_choice}")
    print(f"Computer chooses {computer_choice}")

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "Player wins!"
    else:
        return "Computer wins!"

def main():
    choices = ["rock", "paper", "scissors"]

    while True:
        print("\nRock-Paper-Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        player_choice_index = input("Enter your choice (1, 2, 3, or 4): ")

        if player_choice_index == '4':
            print("Thanks for playing. Goodbye!")
            break

        try:
            player_choice_index = int(player_choice_index)
            if 1 <= player_choice_index <= 3:
                player_choice = choices[player_choice_index - 1]
                computer_choice = random.choice(choices)
                result = play_game(player_choice, computer_choice)
                print(result)
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
