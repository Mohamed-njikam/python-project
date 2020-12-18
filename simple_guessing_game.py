import random

hidden_number = random.randint(0, 9999)

while True:
    print("\n1. Play", "0. Exit", sep="\n")

    choice = input("Please, make a choice from the menu: ")

    if choice in ("1", "Play"):
        print("\nGame started!")
        # the player has a maximum of 3 guesses
        num_guesses = 3
        # if the player run out of guesses, end the game
        while num_guesses != 0:
            # ask the player for a guess
            guess = int(input("Please enter your guess: "))

            # verify if the guess is right
            is_right = guess == hidden_number
            # if the guess is right, output the win message and close the game
            if is_right:
                print("You win!")
                break
            else:
                num_guesses -= 1

        # No guesses remaining
        else:
            print("\nSorry, you lose!!!", f"The hidden number was: {hidden_number}", sep="\n")

    elif choice in ("0", "Exit"):
        print("\nBye!")
        break
