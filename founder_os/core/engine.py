def show_help():
    print("Available commands:")
    print("help - show commands")
    print("hello - say hello")
    print("time - show system status")
    print("exit - close the system")
    return True


def say_hello():
    print("Hello founder")
    return True


def show_time():
    print("System running")
    return True


def shutdown():
    print("Shutting down Founder OS")
    return False


def run_engine():
    print("Founder OS started")

    commands = {
        "help": show_help,
        "hello": say_hello,
        "time": show_time,
        "exit": shutdown
    }

    running = True

    while running:
        command = input("FounderOS > ").strip().lower()

        if command in commands:
            running = commands[command]()
        else:
            print("Unknown command")