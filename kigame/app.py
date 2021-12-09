import sys

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget

from .key import key
from .sprite.manager import sprite_manager

module = sys.modules['__main__']


class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)

        for command in sprite_manager.get_commands():
            self.canvas.add(command)

        Clock.schedule_interval(self._on_draw, 1/60)

    def _on_draw(self, *args):
        if 'update' in dir(module):
            module.update()


class GameApp(App):
    def build(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        return Game()

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        setattr(key, keycode[1], True)
        if 'on_key_down' in dir(module):
            module.on_key_down(keyboard, keycode, text, modifiers)

        if 'on_key' in dir(module):
            module.on_key(keyboard, keycode, text, modifiers)

    def _on_key_up(self, keyboard, keycode):
        setattr(key, keycode[1], False)
        if 'on_key_up' in dir(module):
            module.on_key_up(keyboard, keycode)


app = None


def run():
    global app
    app = GameApp()
    app.run()


if __name__ == "__main__":
    GameApp().run()
