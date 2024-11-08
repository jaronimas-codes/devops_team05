import random

# Initiating new game
list_of_words = ["dog", "cat", "mouse", "monkey", "bucket"]
guess_this_word = random.choice(list_of_words)
word_in_letters = list(guess_this_word)
lives_left = 8
game_is_on = True
empty_letter = "_"
guessed_letters = []

# Display initial game status
def display_current_progress():
    return "".join([letter if letter in guessed_letters else empty_letter for letter in word_in_letters])

def is_word_complete(word):
    return empty_letter not in word

# Main game loop
while game_is_on:
    current_word = display_current_progress()
    guess = input(f"Your word to guess today is {current_word}. Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter. Try a different one.")
        continue

    guessed_letters.append(guess)

    if guess in word_in_letters:
        current_word = display_current_progress()
        if is_word_complete(current_word):
            print(f"Congratulations! You've guessed the word: {current_word}")
            game_is_on = False
        else:
            print(f"Correct! The word so far is: {current_word}. Lives left: {lives_left}")
    else:
        lives_left -= 1
        if lives_left == 0:
            print("Game over. You've run out of lives.")
            game_is_on = False
        else:
            print(f"Wrong guess! The word so far is: {current_word}. Lives left: {lives_left}")

