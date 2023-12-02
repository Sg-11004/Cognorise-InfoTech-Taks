import random

def choose_word():
    word_list = ['apple', 'banana', 'orange', 'grape', 'melon', 'strawberry', 'kiwi']
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6
    hangman_art = [
        "   ____\n  |    |\n      ( )\n      /|\\\n      / \\\n",
        "   ____\n  |    |\n      ( )\n      /|\\\n      /\n",
        "   ____\n  |    |\n      ( )\n      /|\\\n",
        "   ____\n  |    |\n      ( )\n      /|\n",
        "   ____\n  |    |\n      ( )\n      |\n",
        "   ____\n  |    |\n      ( )\n",
        "   ____\n  |    |\n      ( \n",
        "   ____\n  |    |\n",
        "   ____\n",
        ""
    ]

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
            print(hangman_art[6-attempts])
            if attempts == 0:
                print("You lost! The word was:", word_to_guess)
                break
        else:
            print("Good guess!")

        word_display = display_word(word_to_guess, guessed_letters)
        print(word_display)

        if '_' not in word_display:
            print("Congratulations! You've guessed the word:", word_to_guess)
            break
hangman()
