import random

def get_user_choice():
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    while user_score < 10 and computer_score < 10:
        print("\nRock, Paper, Scissors Game")
        user_choice = get_user_choice()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        print(f"Score - You: {user_score}  Computer: {computer_score}")

    if user_score >= 10:
        print("Congratulations! You win the game!")
    else:
        print("Sorry, the computer wins the game.")

play_game()
