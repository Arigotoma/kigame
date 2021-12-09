
class SpriteManager:
    def __init__(self):
        self._commands = []

    def append(self, commands):
        self._commands.append(commands)

    def get_commands(self):
        for command_list in self._commands:
            for command in command_list.get_commands():
                yield command


sprite_manager = SpriteManager()
