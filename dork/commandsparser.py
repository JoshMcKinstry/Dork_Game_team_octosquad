def _start_game():
    return "wellcome to the game!", False

def _exit_game():
    return "Your game has been saved", False

def _show_help():
    return "try typing 'help'", False

def _move_east():
    return "you have moved to east", False

def _move_west():
    return "you have moved to west", False

def _move_north():
    return "you have moved to north", False

def _move_south():
    return "you have moved to south", False



def read():
    return input("> ")

def evaluate(command):
    words_in_command = command.split()
    main_menu = {
         "say": {
         "hello": _start_game,
         "hi"   : _start_game,
         "goodbye" : _exit_game,
         "quit": _exit_game,
         "save" : _exit_game
        },
        "help": {"say": _show_help},
         "go" : {
             "north": _move_north,
             "south": _move_south,
             "west" : _move_west,
             "east" : _move_east
         } 
    }
    for word in words_in_command:
        if word in main_menu:
            sub_menu = main_menu[word]
            for word in words_in_command:
                if word in sub_menu:
                    function = sub_menu[word]
                    return function()

    return "Unknown Command", False

def repl():
    print("starting repl...")
    while True:
        command = read()
        output, should_exit = evaluate(command)
        print(output)
        if should_exit:
            break
    print("ending repl...")

if __name__ == "__main__":
    repl()