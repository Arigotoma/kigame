from shapely.geometry import Polygon

from .base_sprite import BaseSprite
from kivy.graphics import Rectangle, InstructionGroup, Rotate, PushMatrix, PopMatrix


class Sprite(BaseSprite):
    # def __init__(self, image=None, size=(100, 100), pos=(0, 0)):
    #     super().__init__()
    #     self._image = image
    #     self._size = size
    #     self._pos = pos

    def _get_commands(self) -> InstructionGroup:
        self._sprite = Rectangle(texture=self._textures[0], size=self._size, pos=self._pos)
        group = InstructionGroup()
        group.add(self._sprite)

        return group

    @property
    def polygon(self) -> Polygon:
        x, y, width, height = self.x, self.y, self.width, self.height
        return Polygon([(x, y), (x, y + height), (x + width, y + height), (x + width, y), (x, y)])
