import random

name = input('Enter your name: ')
print(f'Hello, {name}')

rating = 0

file = open('rating.txt', 'r+', encoding='utf-8')
file_data = file.readline().split()

if name in file_data:
    rating = int(file_data[file_data.index(name) + 1])


def rock_paper_scissors():
    global rating
    counter_choices = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

    def check(sign1, sign2):
        global rating
        if counter_choices[sign1] == sign2:
            print(f'Sorry, but the computer chose {sign2}')
        elif counter_choices[sign2] == sign1:
            print(f'Well done. The computer chose {sign2} and failed')
            rating += 100
            print(f"{name} {rating}", file=file, flush=True)
        else:
            print(f'There is a draw ({sign2})')
            rating += 50
            print(f"{name} {rating}", file=file, flush=True)

    while True:
        user_choice = input()
        if user_choice == '!exit':
            print('Bye!')
            break
        elif user_choice == '!rating':
            print(f'You rating: {rating}')
        elif user_choice not in counter_choices and user_choice != '!exit':
            print('Invalid input')
        else:
            computer_choice = random.choice(list(counter_choices.values()))
            check(sign1=user_choice, sign2=computer_choice)


def game(user, comp):
    global rating
    if comp in counters:
        print(f'Sorry, but the computer chose {comp}')
    elif comp == user:
        print(f'There is a draw ({comp})')
        rating += 50
        print(f"{name} {rating}", file=file, flush=True)
    else:
        print(f'Well done. The computer chose {comp} and failed')
        rating += 100
        print(f"{name} {rating}", file=file, flush=True)


options = input().split(',')

if "" in options:
    rock_paper_scissors()
else:
    print("Okay, let's start")
    while True:
        choice = input()
        if choice == '!exit':
            print('Bye!')
            break
        elif choice == '!rating':
            print(f'Your rating: {rating}')
        else:
            choice_index = options.index(choice)
            counter_options = options[choice_index + 1:] + options[:choice_index]
            counters = counter_options[:len(options) // 2]
            comp_choice = random.choice(options)
            game(choice, comp_choice)
