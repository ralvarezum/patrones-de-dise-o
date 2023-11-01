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
