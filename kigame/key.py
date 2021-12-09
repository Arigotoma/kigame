from dataclasses import dataclass


@dataclass
class Key:
    spacebar: bool = False
    """Содержит состояние нажат ли пробел"""

    up: bool = False
    """Содержит состояние нажат ли кнопка вверх"""

    down: bool = False
    """Содержит состояние нажат ли кнопка вниз"""

    left: bool = False
    """Содержит состояние нажат ли кнопка влево"""

    right: bool = False
    """Содержит состояние нажат ли кнопка вправо"""


key = Key()
