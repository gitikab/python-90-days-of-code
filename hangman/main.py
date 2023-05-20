import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
guessed_word = ["_"] * len(chosen_word)
lives = 6
end_of_game = False
result = ""

# Show logo
print(logo)

while not end_of_game:
    print(f"{' '.join(guessed_word)}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_word:
        print(f"You have already guessed {guess}")

    guess_correct = False
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            guessed_word[position] = letter
            guess_correct = True

    if not guess_correct:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives = lives - 1

    print(stages[lives])

    if lives == 0:
        end_of_game = True
        result = "You lose"
    elif "_" not in guessed_word:
        end_of_game = True
        result = "You won"


print(f"The word was {chosen_word}")
print(result)
