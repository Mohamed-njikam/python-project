# track if the car is on or not
is_on = False

while True:
    command = input(">").lower()
    # if the user chooses the start command, the car will start
    if command == "start":
        if not is_on:
            is_on = True
            print("Car started...Ready to go!")
        else:
            print("Car already started...")

    # if the user chooses the stop command, the car will stop
    elif command == "stop":
        if is_on:
            is_on = False
            print("Car stopped.")
        else:
            print("Car already stopped...")

    # if the user chooses the quit command, the game terminates
    elif command == "quit":
        print("\nBye!")
        break

    elif command == "help":
        print("\nstart - to start the car", "stop - to stop the car", "quit - to exit\n", sep="\n")

    # if the user enters a command not in the list, tell him that there is no such command and tell him what to do.
    else:
        print("I don't understand that...", "You can type help if you don't know what to do!", sep="\n")
