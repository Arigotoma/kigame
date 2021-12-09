from abc import ABCMeta, abstractmethod

from kivy.event import EventDispatcher

from .manager import sprite_manager


class BaseSprite(EventDispatcher, metaclass=ABCMeta):

    def __init__(self, image=None, size=(100, 100), pos=(0, 0)):
        # self._commands = self._get_commands(*args, **kwargs)
        sprite_manager.append(self)
        self._image = image
        self._size = size
        self._pos = pos

    @abstractmethod
    def get_commands(self, *args, **kwargs):
        pass

    @property
    def x(self):
        return self._sprite.pos[0]

    @x.setter
    def x(self, value):
        self._sprite.pos = (value, self._pos[1])

    @property
    def y(self):
        return self._sprite.pos[1]

    @y.setter
    def y(self, value):
        self._sprite.pos = (self._pos[0], value)
