import random

# Game setup
list_of_words = ["dog", "cat", "mouse", "monkey", "bucket"]
target_word = random.choice(list_of_words)
lives_left = 8
guessed_letters = set()

# Display current game status
def current_progress():
    return "".join(letter if letter in guessed_letters else "_" for letter in target_word)

# Game loop
while lives_left > 0:
    print(f"Word to guess: {current_progress()} | Lives left: {lives_left}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.add(guess)
    
    if set(target_word) <= guessed_letters:
        print(f"Congratulations! You've guessed the word: {target_word}")
        break
    elif guess not in target_word:
        lives_left -= 1
        if lives_left == 0:
            print(f"Game over! The word was: {target_word}")
