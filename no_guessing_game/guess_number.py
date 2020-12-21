from random import randint


computer_number = randint(1, 100)
EASY_CHOICE_TURN = 5
HARD_CHOICE_TURN = 10


def check_answer(user_guess, computer_number, turns):
    """Checks user guess against computer number.
    Returns the number of turns remaining."""
    if user_guess < computer_number:
        print("Too Low")
        return turns - 1
    elif user_guess > computer_number:
        print("Too High")
        return turns - 1
    else:
        print("You Win!")


def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_CHOICE_TURN
    if level == 'hard':
        return HARD_CHOICE_TURN


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print(f"Pssst.... the number is {computer_number}") # For testing
    turns = set_difficulty()

    user_guess = 0

    while user_guess != computer_number:
        print(f"You have {turns} turns remaining") # displays remaining turns after looping
        user_guess = int(input("Make a guess: "))
        turns = check_answer(user_guess, computer_number, turns) # updates the local variable
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return # ends the entire game() function
game()
