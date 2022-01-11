from abc import ABCMeta, abstractmethod
from typing import Union
from math import pi, atan2

from kivy.core.image import Image
from kivy.event import EventDispatcher
from kivy.graphics import InstructionGroup, PopMatrix, PushMatrix, Rotate, Scale
from shapely.geometry import Polygon

from .manager import sprite_manager


class BaseSprite(EventDispatcher, metaclass=ABCMeta):

    def __init__(self,
                 source: str = None,
                 pos: tuple[Union[int, float]] = (0, 0),
                 size: tuple[Union[int, float]] = (None, None),
                 scale: Union[int, float] = 1,
                 angle: Union[int, float] = 0
                 ):
        super().__init__()
        sprite_manager.append(self)

        image = Image(source)
        self._textures = [image.texture]
        self._current_texture = 0

        _size = [
            image.width if size[0] is None else size[0],
            image.height if size[1] is None else size[1]
        ]
        self._init_size = tuple(_size)

        self._init_pos = pos
        self._sprite = None
        self._scale = scale
        self._scale_command = None
        self._angle = angle
        self._rotate_command = None

    def get_commands(self) -> InstructionGroup:
        commands = self._get_commands()
        # TODO: создавать команду только когда она действительно нужна
        if self._angle is not None:
            self._rotate_command = Rotate(angle=self._angle, origin=(self.x + self.width/2, self.y + self.height/2, 0))
            commands.insert(0, self._rotate_command)

        # TODO: создавать команду только когда она действительно нужна
        if self._scale is not None:
            self._scale_command = Scale(self._scale)
            commands.insert(0, self._scale_command)

        if self._angle is not None or self._scale is not None:
            commands.insert(0, PushMatrix())
            commands.add(PopMatrix())

        return commands

    @abstractmethod
    def _get_commands(self, *args, **kwargs):
        pass

    @property
    def _pos(self):
        """Положение спрайта"""
        if self._sprite:
            return self._sprite.pos
        else:
            return self._init_pos

    @_pos.setter
    def _pos(self, pos):
        if self._sprite:
            self._sprite.pos = pos
        else:
            self._init_pos = pos

    @property
    def _size(self):
        """Размер спрайта"""
        if self._sprite:
            return self._sprite.size
        else:
            return self._init_size

    @_size.setter
    def _size(self, size):
        if self._sprite:
            self._sprite.size = size
        else:
            self._init_size = size

    @property
    def angle(self) -> Union[int, float]:
        """Угол поворота спрайта"""
        return self._rotate_command.angle if self._rotate_command else self._angle

    @angle.setter
    def angle(self, angle: Union[int, float]):
        if self._rotate_command:
            self._rotate_command.angle = angle
            self._rotate_command.origin = (self.x + self.width / 2, self.y + self.height / 2, 0)
        else:
            self._angle = angle

    @property
    def scale(self) -> Union[int, float]:
        """Масштаб спрайта"""
        return self._scale_command.angle if self._scale_command else self._scale

    @scale.setter
    def scale(self, scale: Union[int, float]):
        if self._scale_command:
            self._scale_command.scale = scale
        else:
            self._scale = scale

    @property
    def x(self) -> Union[int, float]:
        """Координата x спрайта"""
        return self._pos[0]

    @x.setter
    def x(self, value: Union[int, float]):
        self._pos = (value, self._pos[1])

    @property
    def left(self) -> Union[int, float]:
        """Координата левой границы спрайта"""
        return self._pos[0]

    @left.setter
    def left(self, value: Union[int, float]):
        self._pos = (value, self._pos[1])

    @property
    def right(self) -> Union[int, float]:
        """Координата правой границы спрайта"""
        return self._pos[0] + self._size[0]

    @right.setter
    def right(self, value: Union[int, float]):
        self._pos((value - self._size[0], self._pos[1]))

    @property
    def y(self) -> Union[int, float]:
        """Координата y спрайта"""
        return self._pos[1]

    @y.setter
    def y(self, value: Union[int, float]):
        self._pos = (self._pos[0], value)

    @property
    def bottom(self) -> Union[int, float]:
        """Координата нижней границы спрайта"""
        return self._pos[1]

    @bottom.setter
    def bottom(self, value: Union[int, float]):
        self._pos = (self._pos[0], value)

    @property
    def top(self) -> Union[int, float]:
        """Координата верхней границы спрайта"""
        return self._pos[1] + self._size[1]

    @top.setter
    def top(self, value: Union[int, float]):
        self._pos = (self._pos[0], value - self._size[1])

    @property
    def width(self) -> Union[int, float]:
        """Ширина спрайта"""
        return self._size[0]

    @width.setter
    def width(self, value: Union[int, float]):
        self._size = (value, self._size[1])

    @property
    def height(self) -> Union[int, float]:
        return self._size[1]

    @height.setter
    def height(self, value: Union[int, float]):
        """Высота спрайта"""
        self._size = (self._size[0], value)

    @property
    @abstractmethod
    def polygon(self) -> Polygon:
        pass

    def collide(self, sprite) -> bool:
        """Проверяет пересекается ли текущий спрайт с переданным. Если пересекается, то возвращает True, иначе False."""
        return self.polygon.intersects(sprite.polygon)

    def add_texture(self, source):
        """Добавляет текстуру спрайту."""
        image = Image(source)
        self._textures.append(image.texture)

    def next_texture(self):
        """Переключает на следующую текстуру спрайта."""
        self._current_texture += 1
        if self._current_texture >= len(self._textures):
            self._current_texture = 0

        self._sprite.texture = self._textures[self._current_texture]

    def rotate_to(self, pos_object):
        rel_x = pos_object[0] - self._pos[0]
        rel_y = pos_object[1] - self._pos[1]
        self.angle = int((180 / pi) * -atan2(rel_x, rel_y) + 90)
