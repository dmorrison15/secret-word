import random

random.seed(1)

guessed_letters = []
def go():
    greet_player()
    start_game()
    thank_player()
def start_game():
    while True:
        answer = input("Would you like to start a new round? (Please enter yes or no)\n").strip()
        if answer.lower() == "yes":
            play_round()
        elif answer.lower() == "no":
            break
        else:
            print("Invalid input. Please try again\n")
def greet_player():
    print("\n\nWelcome to secret word! In this game, you will be guessing a random word with 5 lives to guess a letter in the word. For each incorrect guess, you will lose a life. If you guess the word correctly, you win! If you run out of lives, you lose.\n")
def guess_letter(secret_word, displayed_word):
    guess = verify_guess(get_player_guess(), guessed_letters)
    guessed_letters.append(guess)
    return check_guess(guess, secret_word, displayed_word)          
def check_guess(guess, secret_word, displayed_word):
    if guess in secret_word:
        reveal_letters(guess, secret_word, displayed_word)
        print("Good guess!")
        return True
    else:
        print(guess, "is not in the secret word.")
        return False 
def get_player_guess():
    guess = input("\nGuess a letter: ")
    guess = guess.strip()
    return guess.lower()
def play_round():
    secret_word = get_secret_word()
    numlives = 5
    displayed_word = []
    display_blank_word(secret_word, displayed_word)
    while numlives > 0:
        numlives = update_lives(secret_word, displayed_word, numlives)
        if player_wins(displayed_word, secret_word):    
            break
        display_word(displayed_word)
        display_lives(numlives)
    else:    
        game_over(numlives, secret_word)
def reveal_letters(guess, secret_word, displayed_word):
    for i in range(len(secret_word)):
            if secret_word[i] == guess:
                displayed_word[i] = secret_word[i]
def verify_guess(guess, guessed_letters):
    while True:
        if len(guess) != 1 or not guess.isalpha():
            guess = input("Guess is invalid - please try again: ")
            continue
        if guess in guessed_letters:
            guess = input("You already guessed this letter - please try again: ")
            continue
        break
    return guess  
def update_lives(secret_word, displayed_word, numlives):
    if guess_letter(secret_word, displayed_word) == False:
        numlives-=1
    return numlives
def display_lives(numlives):
    if numlives == 1:
        print("\nYou have 1 life left")
    else:
        print("\nYou have", numlives, "lives left")
def player_wins(displayed_word, secret_word):
    if "_" not in displayed_word:
            print("\nYou win! The word is", secret_word)
            return True
    return False
def get_secret_word():
    with open("/home/danimorrison15/secret-word/linuxwords.txt") as f:
        words = f.read().splitlines()
    return random.choice(words)
def game_over(numlives, secret_word):
    if numlives == 0:
        print("\nYou lose, the word was", secret_word, "- Better luck next time")
def thank_player():
    print("Thanks for playing!")
def display_blank_word(secret_word, displayed_word):
    for letter in secret_word:
        displayed_word.append("_")
    display_word(displayed_word)    
def test():
    pass
def display_word(displayed_word):
    print(" ".join(displayed_word))
test()
go()

