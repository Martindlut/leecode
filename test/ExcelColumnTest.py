import unittest
from ExcelColumn import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        result = solution.titleToNumber('AA')
        self.assertEqual(result, 27)


if __name__ == '__main__':
    unittest.main()
