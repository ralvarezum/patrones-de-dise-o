class Command:
    def execute(self):
        pass

class RestartCommand(Command):
    def __init__(self, computer):
        self.computer = computer

    def execute(self):
        self.computer.restart()

class ShutdownCommand(Command):
    def __init__(self, computer):
        self.computer = computer

    def execute(self):
        self.computer.shutdown()

class Computer:
    def restart(self):
        print("Reiniciando la computadora...")

    def shutdown(self):
        print("Apagando la computadora...")

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
        else:
            print("No se ha configurado ningún comando")

computer = Computer()
restart_command = RestartCommand(computer)
shutdown_command = ShutdownCommand(computer)
remote = RemoteControl()

remote.set_command(restart_command)
remote.press_button()

remote.set_command(shutdown_command)
remote.press_button()
