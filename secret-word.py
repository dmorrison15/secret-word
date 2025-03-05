import random

random.seed(1)

guessed_letters = []

def greet_player():
    print("\n\nWelcome to secret word! In this game, you will be guessing a random word with 5 lives to guess a letter in the word. For each incorrect guess, you will lose a life. If you guess the word correctly, you win! If you run out of lives, you lose.\n")

# Returns true if the guess is correct, and false if the guess is incorrect
def guess_letter(secret_word, displayed_word, numlives):
    print("")
    # Get player's guess
    guess = input("Guess a letter: ").strip()
    
    # Make sure guess is valid and hasn't been guessed already
    while True:
        if len(guess) != 1 or not guess.isalpha():
            guess = input("Guess is invalid - please try again: ")
            continue
        if guess in guessed_letters:
            guess = input("You already guessed this letter - please try again: ")
            continue
        break
    guessed_letters.append(guess)
    guess = guess.lower()
    # If guess is correct, reveal where the letter is in the word
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                displayed_word[i] = secret_word[i]
        print("Good guess!")
        # print(" ".join(displayed_word))
        return True
    # If the guess is wrong, player loses a life
    else:
        print(guess, "is not in the secret word.")
        # print(" ".join(displayed_word)) 
        return False          

def play_round():
# Import list of words from text file and select random word
    with open("/home/danimorrison15/secret-word/linuxwords.txt") as f:
        words = f.read().splitlines()
    secret_word = random.choice(words) #cohered
    
    numlives = 5
    
    displayed_word = []
    for letter in secret_word:
        displayed_word.append("_")
    print(" ".join(displayed_word))
    print("")
    
    while numlives > 0:
        if guess_letter(secret_word, displayed_word, numlives) == False:
            numlives-=1
        if "_" not in displayed_word:
            print("You win! The word is", secret_word)
            break
        print(" ".join(displayed_word))
        if numlives == 1:
            print("You have 1 life left")
        else:
            print("You have", numlives, "lives left")
    if numlives == 0:
        print("You lose, the word was", secret_word, "- Better luck next time")


greet_player()

while True:
    answer = input("Would you like to start a new round? (Please enter yes or no)\n")
    if answer.lower() == "yes":
        play_round()
    elif answer.lower() == "no":
        break
    else:
        print("Invalid input. Please try again\n")

print("Thanks for playing!")
    


