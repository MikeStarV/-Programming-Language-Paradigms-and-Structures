import unittest
from data import computers, hdds, comps_hdds
from logic import (
    get_one_to_many,
    get_many_to_many,
    query_b1,
    query_b2,
    query_b3
)


class TestRK2(unittest.TestCase):

    def setUp(self):
        self.one_to_many = get_one_to_many(computers, hdds)
        self.many_to_many = get_many_to_many(computers, hdds, comps_hdds)

    def test_query_b1(self):
        """Проверка задания B1"""
        result = query_b1(self.one_to_many)
        self.assertEqual(
            result,
            [('ADATA SSD Ultimate SU630', 240, 'Игровой ПК')]
        )

    def test_query_b2(self):
        """Проверка задания B2"""
        result = query_b2(self.one_to_many, computers)
        self.assertEqual(
            result,
            [
                ('Игровой ПК', 240),
                ('Офисный ПК', 500),
                ('Сервер', 500)
            ]
        )

    def test_query_b3(self):
        """Проверка задания B3"""
        result = query_b3(self.many_to_many)
        self.assertEqual(result[0][0], 'ADATA SSD Ultimate SU630')
        self.assertEqual(result[-1][0], 'WD Red')


if __name__ == '__main__':
    unittest.main(verbosity=2)
