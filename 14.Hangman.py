import random

def hangman():
    words = ['python', 'algorithm', 'programming', 'hangman', 'challenge']
    word = random.choice(words)
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()

    lives = 6

    print("Welcome to Hangman!")
    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left. Used letters: {' '.join(used_letters)}")
        current_word = [letter if letter in used_letters else '_' for letter in word]
        print('Current word:', ' '.join(current_word))

        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"Letter '{user_letter}' is not in the word.")
        elif user_letter in used_letters:
            print("You already guessed that letter.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print(f"Sorry, you died. The word was '{word}'.")
    else:
        print(f"Congratulations! You guessed the word '{word}'.")

if __name__ == '__main__':
    hangman()
