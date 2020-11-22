import random
import sqlite3

complete_card_number = 0
ID = 0

conn = sqlite3.connect('card.db')

cur = conn.cursor()


# cur.execute("CREATE TABLE card(id INT, number VARCHAR(16), pin TEXT, balance INT DEFAULT 0);")


def insert_info(id_, card_number, card_pin, card_balance):
    cur.execute("INSERT INTO card(id, number, pin, balance) VALUES (?, ?, ?, ?)", (id_, card_number, card_pin,
                                                                                   card_balance))


def call_info(number, code):
    cur.execute("SELECT * FROM card WHERE number=? AND pin=?", (number, code))
    return cur.fetchone()


def luhn_algorithm():
    global complete_card_number
    original_number = bank_industry_identifier + customer_account_number
    starting_index = 0
    lst = []
    drop_the_last_digit = list(original_number)
    for n in drop_the_last_digit:
        lst.append(drop_the_last_digit.index(n, starting_index))
        starting_index += 1
    multiply_by_2 = [int(drop_the_last_digit[n]) * 2 if n % 2 == 0 else int(drop_the_last_digit[n]) for n in lst]
    subtract9 = [n - 9 if n > 9 else n for n in multiply_by_2]
    sum_up = sum(subtract9)
    last_n = str(sum_up)[-1]
    check_digit = 10 - int(last_n)
    if check_digit == 10:
        check_digit = 0
    complete_card_number = "".join([str(n) for n in drop_the_last_digit]) + str(check_digit)


def luhn_algorithm_check(num):
    original_number = "".join(list(str(num))[:-1])
    starting_index = 0
    lst = []
    drop_the_last_digit = list(original_number)
    for n in drop_the_last_digit:
        lst.append(drop_the_last_digit.index(n, starting_index))
        starting_index += 1
    multiply_by_2 = [int(drop_the_last_digit[n]) * 2 if n % 2 == 0 else int(drop_the_last_digit[n]) for n in lst]
    subtract9 = [n - 9 if n > 9 else n for n in multiply_by_2]
    sum_up = sum(subtract9)
    last_n = str(sum_up)[-1]
    check_digit = 10 - int(last_n)
    if check_digit == 10:
        check_digit = 0
    return str(num) == "".join([str(n) for n in drop_the_last_digit]) + str(check_digit)


while True:
    print("1. Create an account", "2. Log into account", "0. Exit", sep="\n")

    choice = input()  # Let him make a choice

    if choice in ("1", "Create an account"):
        bank_industry_identifier = str(400000)
        customer_account_number = "".join([str(random.randint(0, 9)) for n in range(9)])
        pin = "".join([str(random.randint(0, 9)) for n in range(4)])
        balance = 0
        ID = int("".join([n for n in customer_account_number]))

        luhn_algorithm()

        insert_info(ID, complete_card_number, pin, balance)

        conn.commit()

        print("\nYour card number is:", complete_card_number, "Your PIN is:", pin, sep="\n")
        print()

    elif choice in ("2", "Log into account"):
        print("\nEnter your card number:")
        card_num = input()
        print("Enter your PIN:")
        pin_num = input()

        result = call_info(card_num, pin_num)

        if result is None:
            print("\nWrong card number or PIN!\n")

        else:
            print("\nYou have successfully logged in!\n")

            while True:
                print("1. Balance", "2. Add income", "3. Do transfer", "4. Close account",
                      "5. Log out", "0. Exit", sep="\n")
                action = input()
                if action in ("1", "Balance"):
                    print()
                    cur.execute("SELECT balance FROM card WHERE number=?", (card_num,))
                    balance_ = cur.fetchone()
                    print("Balance:", balance_[0])
                    print()

                elif action in ("2", "Add income"):
                    print("Enter income:")
                    income_added = int(input())
                    cur.execute("SELECT balance FROM card WHERE number=?", (card_num,))
                    actual_balance = cur.fetchone()[0]
                    cur.execute("UPDATE card SET balance=?+? WHERE number=?", (actual_balance, income_added, card_num))
                    print("Income was added!")
                    print()
                    conn.commit()

                elif action in ("3", "Do transfer"):
                    print("Transfer", "Enter card number:", sep="\n")
                    receiver_card_number = input()

                    cur.execute("SELECT number FROM card WHERE number=?", (receiver_card_number,))
                    verification = cur.fetchone()

                    # verify the info
                    # receiver card number the same as sender card number
                    if receiver_card_number == card_num:
                        print("You can't transfer money to the same account.")
                        print()

                    elif not luhn_algorithm_check(receiver_card_number):
                        print("Probably you made a mistake in the card number. Please try again!")
                        print()

                    elif verification is None:
                        print("Such a card doesn't exist.")
                        print()

                    # card number is correct
                    else:
                        print("Enter how much money you want to transfer:")
                        income_transferred = int(input())

                        cur.execute("SELECT balance FROM card WHERE number=?", (card_num,))
                        sender_balance = list(cur.fetchone())[0]

                        # sender doesn't have enough money
                        if sender_balance < income_transferred:
                            print("Not enough money!")
                            print()

                        # sender does have money
                        else:
                            cur.execute("SELECT balance FROM card WHERE number=?", (receiver_card_number,))
                            receiver_balance = list(cur.fetchone())[0]

                            cur.execute("UPDATE card SET balance=?+? WHERE number=?", (receiver_balance,
                                                                                       income_transferred,
                                                                                       receiver_card_number))
                            cur.execute("UPDATE card SET balance=?-? WHERE number=?", (sender_balance,
                                                                                       income_transferred,
                                                                                       card_num))

                            print("Success!")
                            print()

                            conn.commit()

                elif action in ("4", "Close account"):
                    cur.execute("DELETE FROM card WHERE number=?", (card_num,))
                    conn.commit()
                    print("The account has been closed!")
                    print()
                    break

                elif action in ("5", "Log out"):
                    print()
                    print("You have successfully logged out!")
                    print()
                    break

                elif action in ("0", "Exit"):
                    print("\nBye!")
                    exit()

    elif choice in ("0", "Exit"):
        print("\nBye!")
        break
conn.close()
