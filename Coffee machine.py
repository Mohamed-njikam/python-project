money_available = 550
water_available = 400
milk_available = 540
coffee_beans_available = 120
disposable_cups = 9


def espresso():
    global water_available, milk_available, milk_available, coffee_beans_available, money_available, disposable_cups
    if water_available < 250 or coffee_beans_available < 16:
        print("""Sorry, not enough water!
        """)
    else:
        water_available -= 250
        milk_available -= 0
        coffee_beans_available -= 16
        money_available += 4
        disposable_cups -= 1
        print("""I have enough resources, making you a coffee!
        """)


def latte():
    global water_available, milk_available, coffee_beans_available, money_available, disposable_cups
    if water_available < 350 or milk_available < 75 or coffee_beans_available < 20:
        print("""Sorry, not enough water!
        """)
    else:
        water_available -= 350
        milk_available -= 75
        coffee_beans_available -= 20
        money_available += 7
        disposable_cups -= 1
        print("""I have enough resources, making you a coffee!
        """)


def cappuccino():
    global water_available, milk_available, coffee_beans_available, money_available, disposable_cups
    if water_available < 200 or milk_available < 100 or coffee_beans_available < 12:
        print("""Sorry, not enough water!
        """)
    else:
        water_available -= 200
        milk_available -= 100
        coffee_beans_available -= 12
        money_available += 6
        disposable_cups -= 1
        print("""I have enough resources, making you a coffee!
        """)


def print_state():
    print(f"""
The coffee machine has:
{water_available} of water
{milk_available} of milk
{coffee_beans_available} of coffee beans
{disposable_cups} of disposable cups
${money_available} of money
""")


class CoffeeMachine:

    def __init__(self):
        self.statement = None

    def user_statement(self):
        self.statement = input()
        return self.statement

    def do_something(self):
        global water_available, milk_available, coffee_beans_available, disposable_cups
        if self.statement == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
            self.user_statement()
            if self.statement in ("1", "espresso"):
                espresso()
            elif self.statement in ("2", "latte"):
                latte()
            elif self.statement in ("3", "cappuccino"):
                cappuccino()
            elif self.statement == "back":
                return

        elif self.statement == "fill":
            print("Write how many ml of water you want to add:")
            water_available += int(self.user_statement())
            print("Write down how many ml of milk you want to add:")
            milk_available += int(self.user_statement())
            print("Write down how many grams of coffee beans you want to add:")
            coffee_beans_available += int(self.user_statement())
            print("Write down how many disposable cups of coffee you want to add:")
            disposable_cups += int(self.user_statement())

        elif self.statement == "take":
            global money_available
            print(f"I gave you ${money_available}")
            money_available = 0

        elif self.statement == "remaining":
            print_state()

    def action(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit): ")
            self.user_statement()
            if self.statement in ("buy", "fill", "take", "remaining"):
                self.do_something()
            elif self.statement == "exit":
                break


coffee = CoffeeMachine()
coffee.action()
