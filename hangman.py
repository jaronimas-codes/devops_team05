import random

# Initiating new game
list_of_words = ["dog", "cat", "mouse", "monkey", "bucket",]
guess_this_word=random.choice(list_of_words)
word_in_letters = list(guess_this_word)
lives_left = 8
game_is_on = True
# game_is_on = False
empty_letter = "_"
guessed_letters = []
guess = input(f"Your word of guess today is {len(word_in_letters)*empty_letter}. Guess the letter." ).lower()
def put_the_letter_in_the_word(list_of_guess, list_of_word_letter):
    fill_the_word = []
    for letter in list_of_word_letter:
        if letter in list_of_guess:
            fill_the_word.append(letter)
        else:
            fill_the_word.append("_")
    return "".join(fill_the_word)
    # print ("".join(fill_the_word))
def finished_the_word(word):
    if "_" in list(word):
        return False
    else:
        return True

while game_is_on:
    guessed_letters.append(guess)
    if guess in word_in_letters:
        put_the_letter_in_the_word(guess, word_in_letters)
        if not finished_the_word(put_the_letter_in_the_word(guessed_letters, word_in_letters)):
            guess = input(f"Your guessed letter is in the word. The word is {put_the_letter_in_the_word(guessed_letters, word_in_letters)}. You already guessed these letters: {[letter for letter in guessed_letters]}. You have left {lives_left} live(s). Try another one.")
        else:
            print("You won the game. Congrats.")
            game_is_on = False
    elif guess not in word_in_letters and lives_left == 1:
        lives_left -= 1
        game_is_on = False
        print("Game over.")
    elif guess not in word_in_letters and lives_left > 1:
        put_the_letter_in_the_word(guess, word_in_letters)
        lives_left -= 1
        guess = input(f"Your guessed letter is not in the word. The word is {put_the_letter_in_the_word(guessed_letters, word_in_letters)}. You already guessed these letters: {[letter for letter in guessed_letters]}. You have left {lives_left} live(s). Try another one.")

