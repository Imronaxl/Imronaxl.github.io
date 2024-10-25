import unittest
import task1


class TestTask1(unittest.TestCase):
    def test_no_smileys(self):
        """Тестирует строку без смайликов."""
        data = r'nobody here'
        result = 0
        self.assertEqual(result, task1.solve(data))

    def test_broken_smileys(self):
        """Тестирует строку с ошибочными смайликами."""
        data = r'Hello =-) =<\ =-) =-here)'
        result = 0
        self.assertEqual(result, task1.solve(data))

    def test_one_smiley(self):
        """Тестирует строку с одним смайликом."""
        data = r'=-\.'
        result = 1
        self.assertEqual(result, task1.solve(data))

    def test_multiple_smileys(self):
        data = r'=-\ =-\ =-\ ='
        result = 3
        self.assertEqual(result, task1.solve(data))

    def test_mixed_content(self):
        """Тестирует строку с текстом, символами и смайликами."""
        data = r'Text and symbols =-\ some other =-\ things =-\='
        result = 3
        self.assertEqual(result, task1.solve(data))

    def test_edge_cases(self):
        data = r'=-=-\=-\=-\ ='
        result = 3
        self.assertEqual(result, task1.solve(data))

if __name__ == '__main__':
    unittest.main()
