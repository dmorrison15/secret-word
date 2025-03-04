import random

random.seed(1)

# Import list of words from text file and select random word
with open("secret-word/linuxwords.txt") as f:
    words = f.read().splitlines()
secret_word = random.choice(words) #cohered


def greet_player():
    print("Welcome to secret word! In this game, you will be guessing a random word with 5 lives to guess a letter in the word. For each incorrect guess, you will lose a life. If you guess the word correctly, you win! If you run out of lives, you lose.")
    


