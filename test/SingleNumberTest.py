import unittest
import SingleNumber


class MyTestCase(unittest.TestCase):
    def test_twosum(self):
        list = [1, 2, 1, 3, 3]
        solution=SingleNumber.Solution()
        result=solution.singleNumber(list)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
