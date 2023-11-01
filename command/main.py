from commands import RestartCommand, ShutdownCommand
from computer import Computer
from remote_control import RemoteControl

computer = Computer()
restart_command = RestartCommand(computer)
shutdown_command = ShutdownCommand(computer)
remote = RemoteControl()

remote.set_command(restart_command)
remote.press_button()

remote.set_command(shutdown_command)
remote.press_button()
