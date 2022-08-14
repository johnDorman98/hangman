# Importing random and the other imports such as the list of words, stages and the logo.
import random
from hangman_words import word_list
from hangman_art import stages, logo, winner_stage, winner_logo

# Variables to store a random word from the list and the length of the word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Setting while loop condition and starting lives.
end_of_game = False
lives = 6

# Displays logo.
print(logo)
print(chosen_word)
# Fills the list with '_' for each letter in the chosen word.
display = []
for _ in range(word_length):
    display += "_"

# Loop runs until 'end_of_game' is True.
while not end_of_game:
    # Gets uses letter guess.
    guess = input("Guess a letter: ").lower()
   
    # Asks the user to enter a new letter if they have enter less then or more then one letter.
    while len(guess) > 1 or len(guess) < 1:
        guess = input("Please guess one letter at a time: ").lower()
        
    # Asks the user for a new letter if they already got one right.
    if guess in display:
        new_guess = input("You have already guessed that letter, try again. ")

    # Loops through in range of the words length and if the user has guessed correctly, it 
    # changes the '_' to that letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    # If the user has guessed incorrectly the user loses a life and is told they guessed 
    # incorrectly, and their remaining lives is displayed.
    if guess not in chosen_word:
        print("Sorry, that letter is not in the word, please try again.")
        
        lives -= 1
        
        print(f"Lives remaining: {lives}")
        
        # If the user runs out of lives the game ends and they lose.
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Using join to display the list in a readable format.
    print(f"{' '.join(display)}")

    # If the 'display' list no longer contains blank spaces the game ends and the user wins.
    if "_" not in display:
        end_of_game = True
        print(winner_stage)
        print(winner_logo)
        break

    # Prints off the stage depending on the users remaining lives.
    print(stages[lives])