import unittest
import task3

class TestTask2(unittest.TestCase):
    def test1(self):
         # Тест 1: каждый день в 12:00
        data = '0 12 * * *'
        result = True
        self.assertEqual(result, task3.solve(data))

    def test2(self):
        # Тест 2: каждые 10 минут с 6 до 18 с пн по пт

        data = "30 14 * * sun"
        result = True
        self.assertEqual(result, task3.solve(data))

    def test3(self):
        # Тест 3: 23:59, 31 декабря, в пятницу
        data = '59 23 31 dec fri'
        result = True
        self.assertEqual(result, task3.solve(data))

    def test4(self):
         # некорректное выражение (минуты > 59)
        data =  "60 14 * * *"
        result = False
        self.assertEqual(result, task3.solve(data))

    def test5(self):
        # некорректное выражение (месяц > 12)
        data =   "30 14 1 13 *"
        result = False

        self.assertEqual(result, task3.solve(data))

if __name__ == '__main__':
    unittest.main()