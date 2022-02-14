from kivy.core.window import Window
from kivy.uix.widget import Widget

from .sprite.manager import sprite_manager


class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)

        for command in sprite_manager.get_commands():
            self.canvas.add(command)
