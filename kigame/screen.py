from kivy.core.window import Window

class Screen:
    @property
    def width(self):
        return Window.size
