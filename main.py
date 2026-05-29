class CommandParser:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, func):
        self.commands[name] = func

    def parse_command(self, command_str):
        command_parts = command_str.split()
        command_name = command_parts[0]
        if command_name in self.commands:
            self.commands[command_name](command_parts[1:])
        else:
            print("Unknown command")

    def start(self):
        while True:
            command_str = input(">>> ")
            self.parse_command(command_str)

def hello_command(args):
    print("Hello, world!")

def echo_command(args):
    print(" ".join(args))

def exit_command(args):
    exit()

parser = CommandParser()
parser.register_command("hello", hello_command)
parser.register_command("echo", echo_command)
parser.register_command("exit", exit_command)
parser.start()