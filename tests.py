import unittest

from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square

class TestFigures(unittest.TestCase):

    # Тест для Прямоугольника
    def test_rectangle_area(self):
        # Создаем прямоугольник 3 на 5
        r = Rectangle("синего", 5, 2)
        # Проверяем: площадь должна быть 15
        self.assertEqual(r.square(), 10)

    def test_rectangle_type(self):
        r = Rectangle("синего", 5, 2)
        # Проверяем, что тип фигуры именно "Прямоугольник"
        self.assertEqual(r.FIGURE_TYPE, "Прямоугольник")

    # Тест для Круга
    def test_circle_area(self):
        import math
        c = Circle("зеленого", 7)
        expected_area = math.pi * (7 ** 2)
        # для float используем AlmostEqual)
        self.assertAlmostEqual(c.square(), expected_area)

    # Тест для Квадрата
    def test_square_area(self):
        s = Square("красный", 5)
        self.assertEqual(s.square(), 25)

    def test_square_repr(self):
        # Проверяем, что метод repr возвращает строку и не падает
        s = Square("красного", 8)
        res = repr(s)
        self.assertIn("Квадрат", res)
        # Проверяем, что есть цвет
        self.assertIn("красного", res)

if __name__ == '__main__':
    unittest.main()