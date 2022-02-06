import unittest
from kigame import Sprite


class SpriteInitializationTestCase(unittest.TestCase):
    def test_default_args(self):
        sprite = Sprite('fly.png')
        commands = sprite.get_commands()
        # Не работает оптимизированная инициализация
        self.assertEqual(len(commands.children), 7, 'Count of commands')

    def test_with_pos(self):
        x = 100
        y = 200
        sprite = Sprite('fly.png', pos=(x, y))
        commands = sprite.get_commands()
        self.assertEqual(sprite._translate_command.x, x, 'x')
        self.assertEqual(sprite._translate_command.y, y, 'y')
        # Не работает оптимизированная инициализация
        self.assertEqual(commands.children[1], sprite._translate_command, 'Position set as Translate command')


if __name__ == '__main__':
    unittest.main()
