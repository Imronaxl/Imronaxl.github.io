import unittest
import task2

class TestTask2(unittest.TestCase):
    def test1(self):
        data = 'Начало урока в 08:30, а окончание в 10:45.'
        result = 'Начало урока в (TBD), а окончание в (TBD).'

        self.assertEqual(result, task2.solve(data))

    def test2(self):
        data =  'Конференция начинается в 12:00:05 и заканчивается в 14:30:59.'
        result = 'Конференция начинается в (TBD) и заканчивается в (TBD).'
        self.assertEqual(result, task2.solve(data))

    def test3(self):
        data = 'Время обеда: 13:00, ужин в 19:15:45.'
        result = 'Время обеда: (TBD), ужин в (TBD).'
        self.assertEqual(result, task2.solve(data))

    def test4(self):
        data = 'Тренировка с 07:15 до 08:45.'
        result = 'Тренировка с (TBD) до (TBD).'
        self.assertEqual(result, task2.solve(data))

    def test5(self):
        data = 'Вечеринка начинается в 22:30 и длится до 00:15.'
        result = 'Вечеринка начинается в (TBD) и длится до (TBD).'

        self.assertEqual(result, task2.solve(data))

if __name__ == '__main__':
    unittest.main()