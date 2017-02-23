import unittest
from ReverseInteger import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        self.assertEqual(solution.reverse(-123), -321)
        self.assertEqual(solution.reverse(1534236469), 0)
        self.assertEqual(solution.reverse(8192), 2918)




if __name__ == '__main__':
    unittest.main()
