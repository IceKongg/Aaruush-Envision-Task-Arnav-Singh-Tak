"""
Rock, Paper, Scissors Game

How to play:
- You play against the computer.
- Enter rock, paper, or scissors.
- The computer randomly selects its choice.
- The winner of each round is shown.
- Scores are tracked until you exit the game.
"""

import random  # Used to generate the computer's random choice


def show_instructions():
    """Displays game rules and instructions to the player"""
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Rules:")
    print("- Rock beats Scissors")
    print("- Scissors beats Paper")
    print("- Paper beats Rock")
    print("Type 'exit' anytime to quit the game.\n")


def get_computer_choice():
    """Returns a random choice for the computer"""
    return random.choice(["rock", "paper", "scissors"])


def decide_winner(player, computer):
    """
    Compares player and computer choices
    Returns:
    - 'player' if player wins
    - 'computer' if computer wins
    - 'draw' if both choose the same
    """
    if player == computer:
        return "draw"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        return "player"
    else:
        return "computer"


def play_game():
    """Main game loop"""
    
    # Initialize scores
    player_score = 0
    computer_score = 0

    show_instructions()

    while True:
        # Take input from the player
        player_choice = input("Enter rock, paper, or scissors: ").lower()

        # Exit condition
        if player_choice == "exit":
            print("\nThanks for playing!")
            print(f"Final Score -> You: {player_score} | Computer: {computer_score}")
            break

        # Handle invalid inputs
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.\n")
            continue

        # Get computer's move
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Decide who won the round
        winner = decide_winner(player_choice, computer_choice)

        if winner == "draw":
            print("It's a draw!\n")
        elif winner == "player":
            print("You win this round!\n")
            player_score += 1
        else:
            print("Computer wins this round!\n")
            computer_score += 1

        # Display current score
        print(f"Current Score -> You: {player_score} | Computer: {computer_score}\n")


# Program entry point
if __name__ == "__main__":
    play_game()

