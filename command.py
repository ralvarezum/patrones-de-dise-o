class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class Light:
    def turn_on(self):
        print("La luz está encendida.")

class RemoteControl:
    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

light = Light()
light_on = LightOnCommand(light)
remote = RemoteControl()
remote.set_command(light_on)

remote.press_button()

