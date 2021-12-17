from abc import ABCMeta, abstractmethod
from numbers import Number

from kivy.event import EventDispatcher
from shapely.geometry import Polygon

from .manager import sprite_manager


class BaseSprite(EventDispatcher, metaclass=ABCMeta):

    def __init__(self,
                 source: str = None,
                 size: tuple[Number] = (100, 100),
                 pos: tuple[Number] = (0, 0)
                 ):
        # self._commands = self._get_commands(*args, **kwargs)
        super().__init__()
        sprite_manager.append(self)
        self._textures = [source]
        self._current_texture = 0
        self._source = source
        self._size = size
        self._pos = pos
        self._sprite = None

    @abstractmethod
    def get_commands(self, *args, **kwargs):
        pass

    @property
    def x(self) -> Number:
        return self._sprite.pos[0]

    @x.setter
    def x(self, value: Number):
        self._sprite.pos = (value, self._pos[1])

    @property
    def y(self) -> Number:
        return self._sprite.pos[1]

    @y.setter
    def y(self, value: Number):
        self._sprite.pos = (self._pos[0], value)

    @abstractmethod
    def get_polygon(self) -> Polygon:
        pass

    def collide(self, sprite) -> bool:
        pass

    def add_texture(self, source):
        self._textures.append(source)

    def next_texture(self):
        self._current_texture += 1
        if self._current_texture >= len(self._textures):
            self._current_texture = 0

        self._sprite.source = self._textures[self._current_texture]

