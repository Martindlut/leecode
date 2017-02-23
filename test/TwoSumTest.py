import unittest
import TwoSum


class MyTestCase(unittest.TestCase):
    def test_twosum(self):
        a=TwoSum.Solution()
        list = [1, 3, 4, 7]
        result = a.twoSum(list, 8)
        self.assertEqual(result == [0, 3])


if __name__ == '__main__':
    unittest.main()
