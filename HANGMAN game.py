

# The game starts here

print("H A N G M A N ")

# menu

while True:

    import random

    # Variables for the game

    used_letters = set()

    english_alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't',
                        'u', 'v', 'w', 'x', 'y', 'z'}

    word_list = ['tout', 'ici', 'rien', 'peu', 'chose', 'autre', 'temps', 'vie', 'accord ', 'monde', 'homme', 'veut',
                 'quelque', 'besoin', 'femme', 'mais', 'comme', 'avant', 'aussi']

    hidden_word = random.choice(word_list)

    hidden_word_class = set(hidden_word)

    hidden_word_hyphen = "-" * len(hidden_word)  # To create the number of hyphens in the word

    hidden_word_hyphen_list = list(hidden_word_hyphen)

    hidden_word_hyphen_string = "".join(hidden_word_hyphen_list)

    lifes = 8

    command = input('\nType "play" to play the game, "exit" to quit: ')

    if command == "play":
        while lifes != 0:
            print(f"\n{hidden_word_hyphen_string}")
            letter = input("Input a letter: ")
            letter_length = len(letter)

            if letter_length > 1:
                print("You should input a single letter")

            elif letter not in english_alphabet:
                print("It is not an ASCII lowercase letter")

            elif letter in used_letters:
                print("You already typed this letter")

            elif letter in hidden_word_class and letter not in hidden_word_hyphen_string and letter not in used_letters:
                used_letters.add(letter)
                hidden_word_hyphen_list[hidden_word.index(letter)] = letter
                hidden_word_hyphen_list[hidden_word.rfind(letter)] = letter
                hidden_word_hyphen_string = "".join(hidden_word_hyphen_list)

                if hidden_word_hyphen_string == hidden_word:
                    print(f"""\n{hidden_word_hyphen_string}
You guessed the word!
You survived!""")
                    hidden_word_hyphen_string = "".join(hidden_word_hyphen_list)
                    break

            elif letter not in hidden_word_class:
                used_letters.add(letter)
                print("No such letter in the word")
                lifes -= 1

        else:
            hidden_word_hyphen_string = "".join(hidden_word_hyphen_list)
            print("You are hanged!")

    elif command == "exit":
        break