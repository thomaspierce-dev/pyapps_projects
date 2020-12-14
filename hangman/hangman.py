import random
from hangman_wordlist import word_list
from hangman_art import stages
from hangman_art import logo
from replit import clear


end_of_game = False # Test case for looping to guess again
lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word) # Get length of chosen word
print(logo)

# Testing Code
# print(f'Pssst, the solution is {chosen_word}.')

'''
initialize empty list called display to to display
characters to the user.
For the length of the randomly chosen word, display the
same number of underscores for the number of letters in that word
'''
display = [] # initialize empty list for display
for _ in range(word_length): # For the word length display underscores
    display += "_"

while not end_of_game:

    # Get the user guess and display
    guess = input("Please guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You already guessed {guess}")
    '''
    Loop through each position in chosen_word (word_length) -- see above
    For each loop, let 'letter' equal the character at chosen_word[position]
    If the 'letter' equals guess through each iteration the
    replace the underscore with the letter at that index [position]
    '''
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    print(f"{' '.join(display)}")

    '''
    check if there are no more "_" left in 'display'. That all letters
    been guessed
    '''

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(stages[lives])


