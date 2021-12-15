from shapely.geometry import Polygon

from .base_sprite import BaseSprite
from kivy.graphics import Rectangle


class Sprite(BaseSprite):
    # def __init__(self, image=None, size=(100, 100), pos=(0, 0)):
    #     super().__init__()
    #     self._image = image
    #     self._size = size
    #     self._pos = pos

    def get_commands(self):
        self._sprite = Rectangle(source=self._source, size=self._size, pos=self._pos)
        return [self._sprite]

    def get_polygon(self):
        return Polygon()

