import random
import numbers

random.seed(1)

def greet_player():
    print("Welcome to secret word! In this game, you will be guessing a random word with 5 lives\nto guess a letter in the word. For each incorrect guess, you will lose a life. If you guess the\nword correctly, you win! If you run out of lives, you lose.\n")

def guess_letter(secret_word, displayed_word, numlives):
    guess = input("Guess a letter: ")
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                displayed_word[i] = secret_word[i]
        print("Good guess!")
        print(" ".join(displayed_word))
        return True
    else:
        print(guess, "is not in the secret word.") 
        return False          

def play_round():
# Import list of words from text file and select random word
    with open("/home/danimorrison15/secret-word/linuxwords.txt") as f:
        words = f.read().splitlines()
    secret_word = random.choice(words) #cohered
    
    numlives = 5
    
    displayed_word = []
    for char in secret_word:
        displayed_word.append("_")
    print(" ".join(displayed_word))
    
    while numlives > 0:
        if guess_letter(secret_word, displayed_word, numlives) == False:
            numlives-=1
        if "_" not in displayed_word:
            print("You win! The word was", secret_word)
            break
        print("You have", numlives, "lives left")
    if numlives == 0:
        print("You lose, the word was", secret_word, "- Better luck next time")




greet_player()

# while True:
#     answer = input("Would you like to start a new round? (Please enter yes or no)\n")
#     if answer.lower() == "yes":
#         play_round()
#     elif answer.lower() == "no":
#         break
#     else:
#         print("Invalid input. Please try again")
play_round()

print("Thanks for playing!")
    


