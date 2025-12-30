import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    while True:
        print("\nChoices: rock, paper, scissors")
        player = input("Enter your choice: ").lower()

        if player not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {player_score}, Computer: {computer_score}")

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing! Final Score:")
            print(f"You: {player_score}, Computer: {computer_score}")
            break

if __name__ == "__main__":
    print("🎮 Welcome to Rock-Paper-Scissors Game!")
    play_game()
