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


class ForwardTestCase(unittest.TestCase):
    def setUp(self):
        self.sprite = Sprite('fly.png')

    def test_default(self):
        self.sprite.forward()
        self.assertEqual(self.sprite.x, 1, 'x')
        self.assertEqual(self.sprite.y, 0, 'y')

    def test_horizontal(self):
        self.sprite.forward(50)
        self.assertEqual(self.sprite.x, 50, 'x')
        self.assertEqual(self.sprite.y, 0, 'y')

    def test_vertical(self):
        self.sprite.angle = 90
        self.sprite.forward(50)
        # Округляем что бы исключить ошибки операций с числами с плавающей точкой
        # Например при угле в 90 градусов после движения получаем смещение по горизонтали на 3.061616997868383e-15
        self.assertEqual(round(self.sprite.x, 10), 0, 'x')
        self.assertEqual(self.sprite.y, 50, 'y')

    def test_at_an_angle(self):
        self.sprite.angle = 45
        self.sprite.forward(50)
        self.assertEqual(round(self.sprite.x, 5), 35.35534, 'x')
        self.assertEqual(round(self.sprite.y, 5), 35.35534, 'y')

    def test_at_an_angle_in_the_negative_direction(self):
        self.sprite.angle = 45
        self.sprite.forward(-50)
        self.assertEqual(round(self.sprite.x, 5), -35.35534, 'x')
        self.assertEqual(round(self.sprite.y, 5), -35.35534, 'y')


if __name__ == '__main__':
    unittest.main()
